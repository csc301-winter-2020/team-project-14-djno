var profile;

$(document).ready(function () {
    $.when(get_user_profile(localStorage.getItem("email")).done(() => {
        // Just to make nav bar more responsive before we migrating it to React.js
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

    }));

});

/* Functions */
function chat(profile) {
    console.log('TODO: chat with profile user');
}

// AJAX Login
// function login () {
//   return $.ajax ({
//     type: 'POST',
//     url: '/login',
//     // The key needs to match your method's input parameter (case-sensitive).
//     data: JSON.stringify ({
//       token_id: 'asd',
//       email: 'at@te.com',
//     }),
//     contentType: 'application/json; charset=utf-8',
//     dataType: 'json',
//     success: data => {
//       console.log (`Login: ${data.login_success}`);
//     },
//     failure: function (errMsg) {
//       console.log (`Login failed: ${errMsg}`);
//     },
//   });
// }

// Retrieve User Profile
function get_user_profile(email) {
    return $.get(`/users/${email}`, function (
        data,
        status
    ) {
        console.log(`Retrieve user profile: ${status}`);
        profile = data.profile;
        console.log(data);
    });
}

// Save Profile
function saveProfile(firstName, lastName, DOB, gender, email) {
    return $.ajax({
        type: 'POST',
        url: '/users',
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            date_of_birth: DOB,
            gender: gender,
            email: email,
        }),
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


function updateSetting(selectObj) {
    const key = selectObj.name;
    const returnObj = {};
    returnObj["email"] = profile.email;

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
            console.log(`Update setting: ${data.update_a_user_settings_success}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}


function signOut() {
    return $.ajax({
        type: 'POST',
        url: '/sign-out',
        success: data => {
            localStorage.clear();

            console.log(`Signout: ${data.sign - out}`);
            location.replace("/index.html");
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}