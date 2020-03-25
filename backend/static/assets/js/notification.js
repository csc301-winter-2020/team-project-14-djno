$(document).ready(function () {
    let socket = io();
    socket.on("connect", function(msg) {
        console.log("successfully connected!")
        console.log("current my email: " + localStorage.getItem("email"))
        socket.emit("listening", {
            email: localStorage.getItem("email"),
            target: "",
            message: "trying to listen..."
        })
    })
    socket.on("chat", function(msg) {
        alert("The person: " + msg["src"])
    })

    socket.on("listened", function(msg) {
        console.log("successfully listening to the server...");
        console.log(msg["message"])
    })

    socket.on("notify", function(msg){
        alert(msg["src"] + " is asking you to join the chat! He/She\
        said " + msg["message"])
    })
})