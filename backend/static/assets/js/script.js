var profile;

$(document).ready(function(){
	$.when(login(), get_user_profile("johnsmith010@gmail.com")).done(() => {
		// Change DOM content
	
		// Home page 
	
		// first name
		document.querySelectorAll("#profile-first-name").forEach((first_name) => {
			first_name.innerText = profile.first_name;
		});
	
		//Profile page
		document.querySelector('input[name="first-name"]').value = profile.first_name;
		document.querySelector('input[name="last-name"]').value = profile.last_name;
		document.querySelector('input[name="email"]').value = profile.email;
		
		// DOB
		const d = new Date(profile.date_of_birth)
		const ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d);
		const mo = new Intl.DateTimeFormat('en', { month: '2-digit' }).format(d);
		const da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d);
		document.querySelector('input[name="dob"]').value = `${ye}-${mo}-${da}`;
		
		// Gender
		let optionExist = document.querySelector(`select[name="gender"] option[value="${profile.gender}"]`);
		if (optionExist) {
			document.querySelector('select[name="gender"]').value = profile.gender;
		} else {
			document.querySelector('select[name="gender"]').value = "null";
		}

		// document.querySelector('input[name="last-name"]').value = profile.last_name;


		/* Listeners */

// // Home Page
// document.querySelector("#decline-request").addEventListener("click", (a) => {
// 	declineRequest(a.target.offsetParent);
// });

// document.querySelector("#chat-request").addEventListener("click", (a) => {
// 	chat(a.target.offsetParent);
// });

// Profile Page
// Edit profile button
const editProfileBtn = document.querySelector("#edit-profile");

editProfileBtn.addEventListener("click", a => {
	if (editProfileBtn.classList.contains("btn-primary")) {
		// When it is an Edit button.
		editProfileBtn.classList.add("btn-info");
		editProfileBtn.classList.remove("btn-primary");
	
		editProfileBtn.innerText = "Save";

		document.querySelectorAll("input, select").forEach((field) => {
			field.disabled = false;
		});

	} else {
		// When it is a Save button.
		editProfileBtn.classList.add("btn-primary");
		editProfileBtn.classList.remove("btn-info");
	
		editProfileBtn.innerText = "Edit";

		document.querySelectorAll("input, select").forEach((field) => {
			field.disabled = true;
		});

	}
});


/* Functions */
function declineRequest(profile) {
	profile.remove();
	console.log("TODO: send declineRequest to server");
}

function chat(profile) {
	console.log("TODO: chat with profile user");
}
	});



});



/* AJAX Login */
function login() {
	return $.ajax({
		type: "POST",
		url: "http://127.0.0.1:8080/login",
		// The key needs to match your method's input parameter (case-sensitive).
		data: JSON.stringify({
			token_id: "asd", 
			email: "at@te.com"
		}),
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		success: data => {console.log(`Login: ${data.login_success}`)},
		failure: function(errMsg) {console.log(`Login failed: ${errMsg}`)}
	});
}

// Retrieve User Profile
function get_user_profile(email) {
	return $.get(`http://127.0.0.1:8080/user/email/${email}`, function(data, status){
		console.log(`Retrieve user profile: ${status}`);
		profile = data.profile;
		console.log(profile);
	});
}







