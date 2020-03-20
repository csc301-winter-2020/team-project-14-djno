$(document).ready(function() {
    // Service worker registration
    sw_registration()

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
})



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


function set_profile(firstName, lastName, date_of_birth, gender, email, description, image_url) {
	data = {
            first_name: firstName,
            last_name: lastName,
            date_of_birth: date_of_birth,
            gender: gender,
            email: email,
            description: description

        }

    if (image_url !== undefined) {
    	data["image_url"] = image_url
    }

    // Create profile
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

    window.addEventListener('load', function() {
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