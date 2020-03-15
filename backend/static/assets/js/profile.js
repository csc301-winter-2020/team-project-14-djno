let profile;

$(document).ready(function () {
    $.when(get_user_profile(localStorage.getItem("email")).done(() => {
        /* Change DOM content */
        document.querySelector('#first-name').value =
            profile.first_name;
        document.querySelector('#last-name').value =
            profile.last_name;
        document.querySelector('#email').value = profile.email;
        document.querySelector('#pfp').src = profile.image_url;
        document.querySelector('#description').value = profile.description;


        // DOB
        const d = new Date(profile.date_of_birth);
        const ye = new Intl.DateTimeFormat('en', {year: 'numeric'}).format(d);
        const mo = new Intl.DateTimeFormat('en', {month: '2-digit'}).format(d);
        const da = (d.getUTCDate() < 10 ? '0' + d.getUTCDate() : d.getUTCDate());

        document.querySelector('input[name="dob"]').value = `${ye}-${mo}-${da}`;

        // Gender
        let optionExist = document.querySelector(
            `select[name="gender"] option[value="${profile.gender}"]`
        );
        if (optionExist) {
            document.querySelector('select[name="gender"]').value = profile.gender;
        } else {
            document.querySelector('select[name="gender"]').value = 'null';
        }

        /* Listeners */

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

        // Edit profile button
        const editProfileBtn = document.querySelector('#edit-profile');

        editProfileBtn.addEventListener('click', () => {
            editProfileBtnEvent(editProfileBtn)
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
    return $.get(`/user/email/${email}`, function (
        data,
        status
    ) {
        console.log(`Retrieve user profile: ${status}`);
        profile = data.profile;
        console.log(profile);
    });
}

// Save Profile
function saveProfile(firstName, lastName, DOB, gender, email, description) {
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
            description: description
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: data => {
            console.log(`Save profile: ${data.create_a_user_success}`);
        },
        failure: function (errMsg) {
            console.log(`Save profile failed: ${errMsg}`);
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
            console.log(`Update setting: ${data.update_settings_success}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}


function signOut() {
    return $.ajax({
        type: 'POST',
        url: '/signout',
        success: data => {
            localStorage.clear();

            console.log(`Signout: ${data.signout}`);
            location.replace("/index.html");
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        },
    });
}

function editProfileBtnEvent(editProfileBtn) {
    if (editProfileBtn.classList.contains('btn-primary')) { // When it is an Edit button.
        // Button style
        editProfileBtn.classList.add('btn-info');
        editProfileBtn.classList.remove('btn-primary');
        editProfileBtn.innerText = 'Save';

        // Enable fields
        document.querySelectorAll('#profile .form-control').forEach(field => {
            if (field.name !== 'email') {   // Email should never be edited.
                field.disabled = false;

                // TODO: security issue: forbid changing email on backend
            }
        });
    } else {    // When it is a Save button.
        // Check if fields values are valid.
        let validSave = true;
        document.querySelectorAll('#profile .form-control').forEach(field => {
            field.classList.remove('is-invalid');  // Reset invalid style.

            if (field.value.length === 0) {
                console.log("${field.name)} is empty or invalid");
                validSave = false;
                field.classList.add('is-invalid');
            }
        });

        if (validSave) {
            // Button style
            editProfileBtn.classList.add('btn-primary');
            editProfileBtn.classList.remove('btn-info');
            editProfileBtn.innerText = 'Edit';

            document.querySelectorAll('input, select').forEach(field => {
                field.disabled = true;  // Disable fields
            });

            // Variables to send to server
            let firstName = document.querySelector('input[name="first-name"]')
                .value;
            let lastName = document.querySelector('input[name="last-name"]')
                .value;
            let DOB = document.querySelector('input[name="dob"]').value;
            let gender = document.querySelector('select[name="gender"]').value;
            let email = document.querySelector('input[name="email"]').value;
            let description = document.querySelector('#description').value;

            // Send to server
            saveProfile(firstName, lastName, DOB, gender, email, description);

        }
    }
}