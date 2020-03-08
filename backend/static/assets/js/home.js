let profile;

$ (document).ready (function () {
  // console.log(document.cookie);
  let data = localStorage.getItem("data")
  console.log("my data is: ", data)
  $.when (login(), get_user_profile (data["email"])).done (() => {
    /* Change DOM content */
    // First name
    document.querySelectorAll ('#profile-first-name').forEach (first_name => {
      first_name.innerText = profile.first_name;
    });

    /* Listeners */

    // Home Page
    document
      .querySelector ('#decline-request')
      .addEventListener ('click', a => {
        declineRequest (a.target.offsetParent);
      });

    document.querySelector ('#chat-request').addEventListener ('click', a => {
      chat (a.target.offsetParent);
    });
  });
});

/* Functions */

function declineRequest (profile) {
  profile.remove ();
  console.log ('TODO: send declineRequest to server');
}

function chat (profile) {
  console.log ('TODO: chat with profile user');
}


// Retrieve User Profile
function get_user_profile (email) {
  console.log("I'm sending..." + email)
  return $.get (`/user/email/${email}`, function (
    data,
    status
  ) {
    console.log (`Retrieve user profile: ${status}`);
    profile = data.profile;
    console.log (profile);
  });
}
