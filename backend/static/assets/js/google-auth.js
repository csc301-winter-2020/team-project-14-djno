console.log("loading...")

function onLoad() {
    signOut();
    gapi.load('auth2,signin2', function () {
        var auth2 = gapi.auth2.init();
        auth2.then(function () {
            // Current values
            var isSignedIn = auth2.isSignedIn.get();
            var currentUser = auth2.currentUser.get();

            if (!isSignedIn) {
                // Rendering g-signin2 button.
                gapi.signin2.render('google-signin-button', {
                    'onsuccess': 'onSignIn'
                });
            }
        });
    });
}

function onSignIn(googleUser) {
// Redirect to home page. FOR TESTING ONLY!!!
    // location.replace("/home.html");
    console.log("asdads")
// Useful data for your client-side scripts:
    const profile = googleUser.getBasicProfile();
    console.log("Login successful");
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

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
    console.log("data>>>>>>>>>>>>>>>");
    console.log(identity);


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
            console.log('Result:', jsonResult)
            if (!jsonResult["login_success"]) {
                location.replace("/home.html")
                signOut()
            }
            else {
                location.replace("/home.html")
            }
        }).catch((error) => {
        // if an error occured it will be logged to the JavaScript console here.
        console.log("An error occured with fetch:", error)
        location.replace("/home.html")
        signOut()
    })


}
function signOut() {
    gapi.auth2.getAuthInstance().signOut();
}
// function onLoad() {
//       gapi.load('auth2', function() {
//         gapi.auth2.init();
//       });
//     }
window.onbeforeunload = function (e) {
    signOut()
};