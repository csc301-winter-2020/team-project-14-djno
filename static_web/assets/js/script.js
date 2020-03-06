/* Listeners */

document.querySelector("#decline-request").addEventListener("click", (a) => {
	declineRequest(a.target.offsetParent);
});

document.querySelector("#chat-request").addEventListener("click", (a) => {
	chat(a.target.offsetParent);
});









/* Functions */
function declineRequest(profile) {
	profile.remove();
	console.log("TODO: send declineRequest to server");
}

function chat(profile) {
	console.log("TODO: chat with profile user");
}