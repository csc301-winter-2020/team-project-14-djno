let userSetting;
let matchingProfile;

$(document).ready(async function () {
    // Print localStorage data
    console.log("Local storage data:\n================================================");
    const dataKeys = Object.keys(localStorage);
    for (i in dataKeys) {
        console.log(`${dataKeys[i]}: ${localStorage.getItem(dataKeys[i])}`);
    }
    console.log("================================================");

    /* Change DOM content */
    // First name
    document.querySelectorAll('#profile-first-name').forEach(first_name => {
        first_name.innerText = localStorage.getItem("first_name");
    });


    let user_setting = await get_user_setting(localStorage.getItem("email"));


    /* Listeners */
    var settingItem = $("select.custom-select.custom-select-sm.d-table.float-right")
        .map(function () {
            // Preload the setting
            preloadSetting.call(this, user_setting);

            // Update any setting once there is a change.
            $(this).change(function () {
                updateSetting(this);
            });
        });

    // Home Page
    document
        .querySelector('#decline-request')
        .addEventListener('click', a => {
            declineRequest(a.target.offsetParent);
        });

    document.querySelector('#chat-request').addEventListener('click', a => {
        chat(a.target.offsetParent);
    });
});

/* Functions */

function declineRequest(profile) {
    profile.remove();
    console.log('TODO: send declineRequest to server');
}

function chat(profile) {
    console.log('TODO: chat with profile user');
}

function updateSetting(selectObj) {
    const key = selectObj.name;
    const returnObj = {};
    returnObj["email"] = localStorage.getItem("email");

    // Currently we only allow update a pair of key
    returnObj[key] = $(selectObj).val();

    console.log(`Updating ${key} to ${returnObj[key]}`);


    return $.ajax({
        type: 'POST',
        url: '/user/settings',

        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(returnObj),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Update setting: ${data.update_settings_success}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}

function selectAllOptions(obj, bool) {
    // The respective Select object.
    const selectObj = obj.closest(".form-group").children[2];

    // Front-end side
    if (bool) {
        for (let i = 0; i < selectObj.options.length; i++) {
            selectObj.options[i].selected = true;
        }
    } else {
        for (let i = 0; i < selectObj.options.length; i++) {
            selectObj.options[i].selected = false;
        }
    }

    // Back-end side
    updateSetting(selectObj);
}

// Retrieve User Profile
function get_user_setting(email) {
    return new Promise((resolve, reject) => {
        $.get(`/user/settings/${email}`, function (
            data,
            status
        ) {
            console.log(`Retrieve user profile: ${status}`);
            if (typeof (data) == "object") {
                resolve(data);
            } else {
                resolve(JSON.parse(data));
            }
        });
    })
}

function preloadSetting(user_setting) {
    // Preload not necessary if user has never changed setting before.
    if (user_setting[this.name] === undefined) {
        return
    }

    for (let i = 0; i < this.options.length; i++) {
        if (user_setting[this.name].includes(this.options[i].value)) {
            this.options[i].selected = true;
        }
    }
}


function makeNewRequest() {
    let validSave = true;

    document.querySelectorAll("[name=title], [name=location], [type=datetime-local], #request-type, [name=message]").forEach(field => {
        // Reset invalid style
        field.classList.remove('invalid');

        if (field.value.length === 0 || field.value === "2020-01-01T00:00" || field.value === "0") {
            console.log(field);
            console.log("is invalid");
            validSave = false;
            field.classList.add('invalid');
        }

    });

    if (validSave) {
        let title = document.querySelector("[name=title]").value;
        let location = document.querySelector("[name=location]").value;
        let datetime = document.querySelector("[type=datetime-local]").value;
        let requestType = document.querySelector("#request-type").value;
        let message = document.querySelector("[name=message]").value;

        let returnObj = {
            "email": localStorage.getItem("email"),
            "request_type": requestType,
            "title": title,
            "location": location,
            "datetime": datetime,
            "message": message
        };


        $.ajax({
            type: 'POST',
            url: '/match',

            // The key needs to match your method's input parameter (case-sensitive).
            data: JSON.stringify(returnObj),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: data => {

                // Change greeting
                document.querySelector("#greetingMessage").innerText = ", You got a matching result!";
                document.querySelector("#greetingDetail").innerText = "This beautiful human being might be able to help you!";

                // List of matching profiles up to top 10 results.
                var e = document.createElement('div');

                // Appending the list of matching profiles.
                for (let i = 0; i < data.length && i < 9; i++) {
                    console.log(`MatchingResult: ${data[i]["email"]}`);

                    // Receive matching profile
                    $.when(get_user_profile(data[i]["email"])).done(() => {

                        let name = matchingProfile["first_name"] + " " + matchingProfile["last_name"];

                        // Adding one matching profile.
                        e.innerHTML += "<div class=\"text-center border rounded-0 shadow-sm profile-box\">\n" +
                            "            <div style=\"height: 50px;background-image: url(&quot;assets/img/bg-pattern.png?h=88366d218f2eda574d88b27e4cb4169d&quot;);background-color: rgba(54,162,177,0);\"></div>\n" +
                            "            <div><img class=\"rounded-circle\" src=\"assets/img/truman.jpg?h=6a7ec640270148575835dffd4d231f7a\" width=\"60px\" style=\"background-color: rgb(255,255,255);padding: 2px;\" height=\"60px\"></div>\n" +
                            "            <div style=\"height: 80px;\">\n" +
                            "                <h4>" + name + "</h4>\n" +
                            "            </div>\n" +
                            "            <div class=\"text-center\" id=\"profile-buttons\"><button class=\"btn btn-success btn-sm\" id=\"chat-request\" type=\"button\" style=\"width: 100px;margin-right: 15px;\">Chat</button><button class=\"btn btn-danger btn-sm\" id=\"decline-request\" type=\"button\" style=\"width: 100px;\">Decline</button></div>\n" +
                            "        </div>";


                        // Finally append the matching profile list
                        document.querySelector("main").appendChild(e)


                    });
                }

                // Hide make request modal.
                $('#modal-2').modal('hide');


            },
            failure: function (errMsg) {
                console.log(`Update setting failed: ${errMsg}`);
            },
        });
    }

}


// Retrieve User Profile
function get_user_profile(email) {
    return $.get(`/user/email/${email}`, function (
        data,
        status
    ) {
        console.log(`Retrieve user profile: ${status}`);
        matchingProfile = data.profile;
        console.log(data);
    });
}