$(document).ready(function () {
    /* Change DOM content */
    document.querySelector('#first-name').value =
        localStorage.first_name;
    document.querySelector('#last-name').value =
        localStorage.last_name;
    document.querySelector('#email').value = localStorage.email;
    document.querySelector('#pfp').src = localStorage.image_url;
    document.querySelector('#description').value = localStorage.description;


    // date_of_birth
    const d = new Date(localStorage.date_of_birth);
    const ye = new Intl.DateTimeFormat('en', {year: 'numeric'}).format(d);
    const mo = new Intl.DateTimeFormat('en', {month: '2-digit'}).format(d);
    const da = (d.getUTCDate() < 10 ? '0' + d.getUTCDate() : d.getUTCDate());

    document.querySelector('input[name="date_of_birth"]').value = `${ye}-${mo}-${da}`;

    // Gender
    let optionExist = document.querySelector(
        `select[name="gender"] option[value="${localStorage.gender}"]`
    );
    if (optionExist) {
        document.querySelector('select[name="gender"]').value = localStorage.gender;
    } else {
        document.querySelector('select[name="gender"]').value = 'null';
    }

    // Edit profile button
    const editProfileBtn = document.querySelector('#edit-profile');

    editProfileBtn.addEventListener('click', () => {
        editProfileBtnEvent(editProfileBtn)
    });

});


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

            document.querySelectorAll('#profile .form-control').forEach(field => {
                field.disabled = true;  // Disable fields
            });

            const data = {
                "first_name": document.querySelector('input[name="first-name"]')
                    .value,
                "last_name": document.querySelector('input[name="last-name"]')
                    .value,
                "date_of_birth": document.querySelector('input[name="date_of_birth"]').value,
                "gender": document.querySelector('select[name="gender"]').value,
                "description": document.querySelector('#description').value
            };

            // Only request changes to server when needed
            for (let field in data) {
                if (data[field] !== localStorage[field]) {
                    // Update local storage
                    set_local_storage(data);

                    // Send to server
                    set_profile(localStorage.first_name, localStorage.last_name, localStorage.date_of_birth, localStorage.gender, localStorage.email, localStorage.description);

                    return
                }
            }


        }
    }
}