var profile;

$ (document).ready (function () {
  $.when (login (), get_user_profile ('johnsmith010@gmail.com')).done (() => {
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

// AJAX Login
function login () {
  return $.ajax ({
    type: 'POST',
    url: 'http://127.0.0.1:8080/login',
    // The key needs to match your method's input parameter (case-sensitive).
    data: JSON.stringify ({
      token_id: 'asd',
      email: 'at@te.com',
    }),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: data => {
      console.log (`Login: ${data.login_success}`);
    },
    failure: function (errMsg) {
      console.log (`Login failed: ${errMsg}`);
    },
  });
}

// Retrieve User Profile
function get_user_profile (email) {
  return $.get (`http://127.0.0.1:8080/user/email/${email}`, function (
    data,
    status
  ) {
    console.log (`Retrieve user profile: ${status}`);
    profile = data.profile;
    console.log (profile);
  });
}
