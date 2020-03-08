function onSignIn(googleUser) {
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
    console.log("ID Token: " + id_token);


    var identity = {"ID": profile.getId(), "Email": profile.getEmail()};
    document.cookie = identity;

    const url = '/auth';
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
            console.log('Success');
            return res.json()
            ////
        })
        .then((jsonResult) => {
            // Although this is a post request, sometimes you might return JSON as well
            console.log('Result:', jsonResult)

        }).catch((error) => {
        // if an error occured it will be logged to the JavaScript console here.
        console.log("An error occured with fetch:", error)
    })


}


function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
        document.cookie = null;
        console.log(document.cookie);
    });

}

function alertCookie() {
    alert(document.cookie);
}