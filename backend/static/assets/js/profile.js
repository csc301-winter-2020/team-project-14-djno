$(document).ready(function () {
    /* Change DOM content */
    document.querySelector('#first-name').value =
        localStorage.first_name;
    document.querySelector('#last-name').value =
        localStorage.last_name;
    document.querySelector('#email').value = localStorage.email;
    document.querySelector('#pfp').src = localStorage.image_url;
    document.querySelector('#description').value = localStorage.description;


    // DOB
    const d = new Date(localStorage.date_of_birth);
    const ye = new Intl.DateTimeFormat('en', {year: 'numeric'}).format(d);
    const mo = new Intl.DateTimeFormat('en', {month: '2-digit'}).format(d);
    const da = (d.getUTCDate() < 10 ? '0' + d.getUTCDate() : d.getUTCDate());

    document.querySelector('input[name="dob"]').value = `${ye}-${mo}-${da}`;

    // Gender
    let optionExist = document.querySelector(
        `select[name="gender"] option[value="${localStorage.gender}"]`
    );
    if (optionExist) {
        document.querySelector('select[name="gender"]').value = localStorage.gender;
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

});


/* Functions */
function chat(profile) {
    console.log('TODO: chat with profile user');
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
    returnObj["email"] = localStorage.email;

    // Currently we only allow update a pair of key
    returnObj[key] = $(selectObj).val();

    console.log(`Updating ${key} to ${returnObj[key]}`);


    return $.ajax({
        type: 'POST',
        url: '/users/settings',

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

            console.log(`Signout: ${data.sign_out}`);
            location.replace("/login.html");
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
                console.log(field.name);
                console.log("is empty or invalid");
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

            const data = {
                "first_name": document.querySelector('input[name="first-name"]')
                    .value,
                "last_name": document.querySelector('input[name="last-name"]')
                    .value,
                "DOB": document.querySelector('input[name="dob"]').value,
                "gender": document.querySelector('select[name="gender"]').value,
                "description": document.querySelector('#description').value
            };

            // Update local storage
            set_local_storage(data);


            // Send to server
            saveProfile(localStorage.first_name, localStorage.last_name, localStorage.DOB, localStorage.gender, localStorage.email, localStorage.description);

        }
    }
}