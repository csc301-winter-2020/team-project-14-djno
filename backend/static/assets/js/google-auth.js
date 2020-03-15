// function onLoad() {
//     signOut();
//     // gapi.load('auth2,signin2', function () {
//     //     var auth2 = gapi.auth2.init();
//     //     auth2.then(function () {
//     //         // Current values
//     //         var isSignedIn = auth2.isSignedIn.get();
//     //         var currentUser = auth2.currentUser.get();
//
//     //         if (!isSignedIn) {
//     //             // Rendering g-signin2 button.
//     //             gapi.signin2.render('google-signin-button', {
//     //                 'onsuccess': 'onSignIn'
//     //             });
//     //         }
//     //     });
//     // });
// }

function onSignIn(googleUser) {
// Useful data for your client-side scripts:
    const profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());
    let data = {
        "id": profile.getId(),
        "name": profile.getName(),
        "imageUrl": profile.getImageUrl(),
        "email": profile.getEmail(),
        "first_name": profile.getGivenName(),
        "last_name": profile.getFamilyName(),
        "image_url": profile.getImageUrl()
    };


    // The ID token for passing to the backend:
    var id_token = googleUser.getAuthResponse().id_token;

    var identity = {"token_id": profile.getId(), "email": profile.getEmail()};
    const url = '/login';
    // Create the request constructor with all the parameters we need
    const request = new Request(url, {
        method: 'post',
        body: JSON.stringify(identity),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
    });
    // Send the request
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
            // Although this is a post request, sometimes you might return JSON as well
            console.log('Result:', jsonResult);
            if (!jsonResult["login_success"]) {
                location.replace("/index.html");
                signOut()
            } else {
                console.log("login successful!");
                for (key in data) {
                    localStorage.setItem(key, data[key])
                }

                $.when(get_user_profile(data["email"]).done((e) => {
                    // If user doesn't exist
                    if (!e["profile_exist"]) {
                        // TODO popup a create user page in D3
                        let DOB = "2020-01-01";
                        let age = (new Date() - new Date(DOB)) / (1000 * 3600 * 24 * 365);
                        let description = "";

                        // Create a profile
                        $.when(saveProfile(data["first_name"], data["last_name"], DOB, "Male", data["email"], data["image_url"], age, description)).done((e) => {
                            console.log("profile created");
                            var auth2 = gapi.auth2.getAuthInstance();
                            auth2.disconnect();
                            location.replace("/home.html")
                        });
                    } else {
                        var auth2 = gapi.auth2.getAuthInstance();
                        auth2.disconnect();
                        location.replace("/home.html")
                    }

                }));


            }
        }).catch((error) => {
        // if an error occured it will be logged to the JavaScript console here.
        console.log("An error occured with fetch:", error);
        location.replace("/index.html");
        signOut()
    })


}

function signOut() {
    gapi.auth2.getAuthInstance().signOut();
    localStorage.clear();
}

// function onLoad() {
//       gapi.load('auth2', function() {
//         gapi.auth2.init();
//       });
//     }
// window.onbeforeunload = function (e) {
//     signOut()
// };


// Retrieve User Profile
function get_user_profile(email) {
    return $.get(`/users/${email}`, function (
        data,
        status
    ) {
        console.log(`Retrieve user profile: ${status}`);
        profile = data.profile;
    });
}

// Save Profile
function saveProfile(firstName, lastName, DOB, gender, email, image_url, age, description) {
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
            image_url: image_url,
            age: age,
            description: description

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
