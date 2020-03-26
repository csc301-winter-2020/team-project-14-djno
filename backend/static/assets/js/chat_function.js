function scroll_to_bottom() {
    // Scroll to the bottom of the chat box
    const chatBoxScrollHeight = document.querySelector("#chat-box").scrollHeight;
    document.querySelector("#chat-box").scrollTo(0, chatBoxScrollHeight);
}

$(document).ready(function () {
    // let messages = [];
    // let user_email = (JSON.parse(localStorage.getItem("to")))["email"];;
    // localStorage.setItem(user_email, JSON.stringify(messages));

    $("#Message-send-button").attr("disabled", "disabled");
    let sample_user = `<a href="#" class="user" class="list-group-item list-group-item-action list-group-item-light rounded-0">
   <div class="media"><img src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg"
      alt="user" width="50" class="rounded-circle">
    <div class="media-body ml-4">
      <div class="d-flex align-items-center justify-content-between">
      <h6 class="mb-0" class="user_name">
        ${"Example User"}
        </h6>
            <small class="small font-weight-bold">${date()}</small>
      </div>
    </div>
  </div>
</a>
`;
    $("#contact-list").append(sample_user);
    $("#contact-list").append(newUser());

    let is_connected = false;
    var socket = io();
    socket.on("chat", function (msg) {
        console.log("message is....");
        console.log(msg);
        //reveice message
        receiveMessage(msg);
        // messages = (JSON.parse(localStorage.getItem(msg["src"])));
        // messages.push({email:msg["src"],message:msg["message"], date: date()})
        // localStorage.setItem(msg["src"], JSON.stringify(messages));
    });
    socket.on("connect", function () {
        socket.emit("join", {
            email: localStorage.getItem("email"),
            target: "",
            message: "connect"
        });
        console.log("emitted!");
    });
    socket.on("joined", function (msg) {
        console.log("joined");
        console.log(msg);
        $("#Message-send-button").removeAttr("disabled");
        //send message
        $("#Message-send-button").click(function (event) {
            event.preventDefault();

            const message = $("#type-message").val();

            // Prevent sending empty message
            if (message.length === 0) {
                return
            }

            sendMessage();
            socket.emit("chat", {
                email: localStorage.getItem("email"),
                target: JSON.parse(localStorage.getItem("to"))["email"],
                message: message
            });

            // Reset input field
            this.offsetParent.parentElement.reset();

            scroll_to_bottom();

            // $("#Message-send-button").attr("disabled", "disabled");
            // setTimeout(() => {
            //   $("#Message-send-button").removeAttr("disabled");
            // }, 500);

            // messages = (JSON.parse(localStorage.getItem(target)));
            // messages.push({email:localStorage.getItem("email"),message:$("#type-message").val(), date: date()})
            // localStorage.setItem(msg["src"], JSON.stringify(messages));
        });
    });

    socket.on("failed", function (msg) {
        console.log("failed!");
        console.log(msg);
    });
});

function date() {
    let today = new Date();
    let date =
        today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
    let time =
        today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    let dateTime = date + " " + time;
    return dateTime;
}

function newUser() {
    new_user = JSON.parse(localStorage.getItem("to"));
    let user = `

                <a href="#" class="user" class="list-group-item list-group-item-action list-group-item-light rounded-0">
                 <div class="media"><img src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg"
                    alt="user" width="50" class="rounded-circle">
                  <div class="media-body ml-4">
                    <div class="d-flex align-items-center justify-content-between">
                    <h6 class="mb-0" class="user_name">
                      ${new_user["name"]}
                      </h6>
                          <small class="small font-weight-bold">${date()}</small>
                    </div>
                  </div>
                </div>
              </a>

              `;

    return user;
}

function sendMessage() {
    if ($("#type-message").val()) {
        const message = $("#type-message").val();

        let ReMessage = `
            <!-- Reciever Message-->
            <div class="media w-75 ml-auto">
            <div class="media-body">
                <div class="bg-primary rounded py-2 px-3">
                <p class="text-small mb-0 text-white">${message}</p>
                </div>
                <p class="small text-muted">${date()}</p>
            </div>
            </div>
    
                `;

        $("#chat-box").append(ReMessage);
    }
}

function receiveMessage(msg) {
    let from = msg["src"];
    let message = msg["message"];

    let reMessage = `
                <div class="media w-75">
                  <div class="media-body">
                    <div class="bg-light rounded py-2 px-3">
                      <p class="text-small mb-0 text-muted">${message}</p>
                    </div>
                    <p class="small text-muted">${date()}</p>
                  </div>
              </div> 
  `;
    $("#chat-box").append(reMessage);

    scroll_to_bottom();
}

// function loadPreviousMessage() {

// }
