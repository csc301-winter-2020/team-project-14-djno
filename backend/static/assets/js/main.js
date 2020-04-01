$(document).ready(function () {
    // Service worker registration
    sw_registration();

    // Print localStorage data
    console.log("Local storage data:\n================================================");
    const dataKeys = Object.keys(localStorage);
    for (let i in dataKeys) {
        console.log(`${dataKeys[i]}: ${localStorage.getItem(dataKeys[i])}`);
    }
    console.log("================================================");

    // Make nav bar faster/more responsive before we migrating it to React.js
    if (document.querySelector(".nav")) {

        document.querySelectorAll(".nav-item").forEach(item => {
            item.addEventListener('click', a => {
                // remove active style on all nav items
                document.querySelectorAll(".nav-item").forEach(other => {
                    other.firstChild.classList.remove("active");
                });

                // add active style on clicked item
                a.target.firstChild.classList.add("active");
                a.target.classList.add("active")
            });
        });

    }

    /* Listeners */
    let at_least_one_enabled = false
    $("#setting-modal .toggle")
        .map(function () {
            // Preload the setting
            preloadSetting.call(this);

            if (!this.classList.contains("off")) {  // if it is enabled
                at_least_one_enabled = true;
            }

            // Update any setting once there is a change.
            mutationObserver.observe(this, {attributes: true});
        });
    
    if (!at_least_one_enabled) {    // show the setting modal if none of the settinh is enabled. Usually apply to new user
        $("#setting-modal").modal('show');
    }


});

function mutationCallback(mutationsList) {
    mutationsList.forEach(mutation => {
        if (mutation.attributeName === "class") {
            const key = mutation.target.firstChild.id;
            const value = !mutation.target.classList.contains("off");

            // Update setting only when new value does not match the value in local storage.
            if (localStorage[key] !== value.toString()) {
                set_local_storage({[key]: value});  // update on local storage
                updateSetting(key, value);  // update on the server
            }
        }
    });
}

const mutationObserver = new MutationObserver(mutationCallback);

function preloadSetting() {
    // Preload not necessary if user has never changed setting before.
    if (localStorage[this.firstChild.id] === undefined) {
        console.error(`${this.firstChild.id} is not in Local Storage`);
        return
    }

    if (localStorage[this.firstChild.id] === "true") { // When it is set to true
        this.classList.add("btn-success");
        this.classList.remove("off", "btn-default");
    } else {    // When it is set to false
        this.classList.add("off", "btn-default");
        this.classList.remove("btn-success")
    }
}


function set_local_storage(data) {
    for (let key in data) {
        localStorage.setItem(key, data[key])
    }
}

// Retrieve User Setting
function get_user_setting(email) {
    return new Promise((resolve, reject) => {
        $.get(`/users/settings/${email}`, function (
            data,
            status
        ) {
            console.log(`Retrieve user setting: ${status}`);
            console.log(data);

            // User setting should not be an empty object
            if (Object.keys(data).length === 0 && data.constructor === Object) {
                console.error("user setting is not initialized");
                resolve(data);
            }

            resolve(JSON.parse(data));

        });
    })
}


function updateSetting(key, value) {
    const returnObj = {};
    returnObj["email"] = localStorage.getItem("email");

    // We only allow update a pair of key because of the toggling nature
    returnObj[key] = value;

    return $.ajax({
        type: 'POST',
        url: '/users/settings',

        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(returnObj),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Updated ${key} to ${returnObj[key]}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}

// Retrieve User Profile
function get_user_profile(email) {
    return $.get(`/users/${email}`, function (data) {
        profile = data.profile;
    });
}

function set_profile(firstName, lastName, date_of_birth, gender, email, description, image_url) {
    data = {
        first_name: firstName,
        last_name: lastName,
        date_of_birth: date_of_birth,
        gender: gender,
        email: email,
        description: description

    };

    if (image_url !== undefined) {
        data["image_url"] = image_url
    }

    return $.ajax({
        type: 'POST',
        url: '/users',
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Create profile: ${data.create_a_user_success}`);
        },
        failure: function (errMsg) {
            console.log(`Create profile failed: ${errMsg}`);
        },
    });
}

function sw_registration() {
    if (!('serviceWorker' in navigator)) {
        console.log('sw not supported');
        return;
    }

    window.addEventListener('load', function () {
        navigator.serviceWorker.register(
            'service-worker.js')
            .then(reg => {
                console.log('Service worker registered! 😎', reg);
            })
            .catch(err => {
                console.log('😥 Service worker registration failed: ', err);
            });
    });
}

function acceptRequest() {
    console.log("User accepted request");
    let requester_email = document.querySelector("#accept-request-modal .modal-body #requester-email").innerText;
    console.log(`Do something with ${requester_email}`)
}

function initAcceptRequestModal(email, message) {
    document.querySelector("#accept-request-modal .modal-body #requester-email").innerText = email;
    document.querySelector("#accept-request-modal .modal-body #requester-message").innerText = message
}