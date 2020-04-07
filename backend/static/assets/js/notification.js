$(document).ready(function () {
    let socket = io();
    socket.on("connect", function (msg) {
        console.log("Connected to socket!");
        socket.emit("listening", {
            email: localStorage.getItem("email"),
            target: "",
            message: "trying to listen..."
        })
    });
    socket.on("chat", function (msg) {
        alert("The person: " + msg["src"])
    });

    socket.on("listened", function (msg) {
        console.log(msg["message"])
    });

    socket.on("notify", function (msg) {
        console.log("getting...");
        localStorage.setItem("candidate", msg["src"]);
        $("#notification").modal({
            show: true
        });
        let cur_request = msg["src"] + " is asking you to join the chat! He/She\
                                        said " + msg["message"];
        $("#notification_field").text(cur_request)
    })
});

function goChat() {
    localStorage.setItem("to", JSON.stringify({
        email: localStorage.getItem("candidate"),
        name: "requester"
    }));
    localStorage.removeItem("candidate");
    location.replace("/chat.html")
}

function cancelChat() {
    localStorage.removeItem("candidate")
}
