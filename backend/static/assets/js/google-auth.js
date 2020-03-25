function redirect_to_main_app() {
    gapi.auth2.getAuthInstance().disconnect();  // Disconnect from google auth.
    location.replace("/index.html") // Redirect to the main app.
}

function onSignIn(googleUser) {
    // Listener for the signup modal
    $('#signup-modal').on('hide.bs.modal', function (e) {
        /* Disconnect from current auth session if user does not proceed completing personal information*/
        const auth2 = gapi.auth2.getAuthInstance();
        auth2.disconnect();
    });

    // Data received from Google
    const profile = googleUser.getBasicProfile();
    const identity = {"token_id": profile.getId(), "email": profile.getEmail()};

    // Create the request constructor with all the parameters we need
    const request = new Request('/login', {
        method: 'post',
        body: JSON.stringify(identity),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
    });

    function preload_info() {
        // Preload the personal information from Google Auth
        document.querySelector('#first-name').value =
            profile.getGivenName();
        document.querySelector('#last-name').value =
            profile.getFamilyName();
        document.querySelector('#email').value = profile.getEmail();
    }

    // Send the request once signed in using Google auth
    fetch(request)
        .then((res) => {
            //// Do not write any code here
            // Logs success if server accepted the request
            //   You should still check to make sure the blocking was saved properly
            //   to the text files on the server.
            return res.json()
            ////
        })
        .then((jsonResult) => {
            console.log('Connection to server:', jsonResult);

            // Make sure sign out from Google auth if fail to connect to server.
            if (!jsonResult["login_success"]) {
                signOut();
                return
            }

            // Cache necessary information
            const data = {
                "id": profile.getId(),
                "image_url": profile.getImageUrl(),
                "email": profile.getEmail()
            };
            set_local_storage(data);


            $.when(get_user_profile(profile.getEmail()).done(async function (e) {
                if (!e["profile_exist"]) {
                    // Continue signup process if user does not exist in the database
                    preload_info();
                    $("#signup-modal").modal("show");

                } else {
                    // Cache user profile received from server to local storage
                    set_local_storage(e.profile);

                    // Cache user setting as well
                    const user_setting = await get_user_setting(profile.getEmail());
                    set_local_storage(user_setting);

                    // Existing user.
                    redirect_to_main_app();
                }
            }));

        }).catch((error) => {
        // if an error occurred it will be logged to the JavaScript console here.
        console.log("An error occured with fetch:", error);
        signOut()
    })
}


function signOut() {
    gapi.auth2.getAuthInstance().signOut();
    localStorage.clear();
}


async function sign_up() {
    // Check if fields values are valid.
    let validSave = true;
    document.querySelectorAll('#signup-form .form-control').forEach(field => {

        field.classList.remove('is-invalid');  // Reset invalid style.

        if (field.value.length === 0) {
            console.log(field.name);
            console.log("is empty or invalid");
            validSave = false;
            field.classList.add('is-invalid');
        }
    });

    if (validSave) {
        const data = {
            "first_name": document.querySelector('input[name="first-name"]')
                .value,
            "last_name": document.querySelector('input[name="last-name"]')
                .value,
            "date_of_birth": document.querySelector('input[name="date_of_birth"]').value,
            "gender": document.querySelector('select[name="gender"]').value,
            "description": document.querySelector('#description').value
        };

        // Update local storage
        set_local_storage(data);

        // Cache user setting as well
        const user_setting = await get_user_setting(localStorage["email"]);
        set_local_storage(user_setting);


        // Create a profile and send to server
        $.when(set_profile(data["first_name"], data["last_name"], data["date_of_birth"], data["gender"], localStorage.email, data["description"], localStorage.image_url)).done(() => {
            redirect_to_main_app()
        });
    }
}