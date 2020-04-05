$(document).ready(function () {
  let me = localStorage.getItem("email");
  let to = JSON.parse(localStorage.getItem("to"))["email"];
  let chat = { email: me, to: to, chat_function: [] };
  let contact = {
    name: JSON.parse(localStorage.getItem("to"))["name"],
    email: to,
    date: date(),
  };
  let chats;
  let contacts;
  let chat_history;

  // template for chat history storing in chat_funciton {}
  // let chat_history= {"target_email1" : { "name": , "messages": [{"src":, "message": }], "date": }};

  // check if "contacts" exsits
  if (JSON.parse(localStorage.getItem("contacts"))) {
    contacts = JSON.parse(localStorage.getItem("contacts"));
    chats = JSON.parse(localStorage.getItem("chats"));
  } else {
    chats = [];
    chats.push(chat);
    localStorage.setItem("chats", JSON.stringify(chats));
    contacts = [];
    contacts.push(contact);
    localStorage.setItem("contacts", JSON.stringify(contacts));
  }

  $("#Message-send-button").attr("disabled", "disabled");
  newUser(contacts, contact, chat, chats);

  // Web Socket
  let is_connected = false;
  var socket = io();
  socket.on("chat", function (msg) {
    console.log("message is");
    console.log(msg);
    //reveice message
    receiveMessage(msg, date());

    // store information into localstorage
    let target = JSON.parse(localStorage.getItem("to"))["email"];
    let message = msg["message"];
    let chats = JSON.parse(localStorage.getItem("chats"));
    let counter = 0;
    console.log("add send message into local storage");
    for (user_chat of chats) {
      if (user_chat["to"] == target) {
        chat_history = { src: target, message: message, date: date() };

        user_chat["chat_function"].push(chat_history);
        chats[counter] = user_chat;
        localStorage.setItem("chats", JSON.stringify(chats));
      }
      counter++;
    }
  });
  socket.on("connect", function () {
    socket.emit("join", {
      email: localStorage.getItem("email"),
      target: "",
      message: "connect",
    });
    // console.log("emitted!");
  });
  socket.on("joined", function (msg) {
    // console.log("joined");
    // console.log(msg);
    $("#Message-send-button").removeAttr("disabled");
    //send message
    $("#Message-send-button").click(function (event) {
      event.preventDefault();
      if ($("#type-message").val()) {
        const message = $("#type-message").val();
        sendMessage(message, date());
      }
      socket.emit("chat", {
        email: localStorage.getItem("email"),
        target: JSON.parse(localStorage.getItem("to"))["email"],
        message: $("#type-message").val(),
      });

      // store information into localstorage
      let target = JSON.parse(localStorage.getItem("to"))["email"];
      let message = $("#type-message").val();
      let chats = JSON.parse(localStorage.getItem("chats"));
      let counter = 0;
      console.log("add send message into local storage");
      for (user_chat of chats) {
        if (user_chat["to"] == target) {
          chat_history = { src: me, message: message, date: date() };

          user_chat["chat_function"].push(chat_history);
          chats[counter] = user_chat;
          localStorage.setItem("chats", JSON.stringify(chats));
        }
        counter++;
      }

      $("#type-message").val("");
      $("#Message-send-button").attr("disabled", "disabled");
      setTimeout(() => {
        $("#Message-send-button").removeAttr("disabled");
      }, 500);
    });

    socket.on("failed", function (msg) {
      console.log("failed!");
      console.log(msg);
    });

    // switch user interface
    const buttons = document.querySelectorAll(".user");
    for (const button of buttons) {
      button.addEventListener("click", function (event) {
        to = $(this).attr("email");
        console.log(to);
        $("#chat-box").empty();
        switch_Users_chatbox(to);
      });
    }
  });

  // switch user interface
  const buttons = document.querySelectorAll(".user");
  for (const button of buttons) {
    button.addEventListener("click", function(event) {
      to = $(this).attr("email");
      console.log(to);
      $("#chat-box").empty();
      switch_Users_chatbox(to);
    });
  }
});

function scroll_to_bottom() {
  // Scroll to the bottom of the chat box
  const chatBoxScrollHeight = document.querySelector("#chat-box").scrollHeight;
  document.querySelector("#chat-box").scrollTo(0, chatBoxScrollHeight);
}

function date() {
  let today = new Date();
  let date =
    today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
  let time =
    today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  let dateTime = date + " " + time;
  return dateTime;
}

function newUser(contacts, contact, chat, chats) {
  console.log("====add new user====");

  let user_exsits = false;
  //check and store contact if it doesn't exsit
  for (user of JSON.parse(localStorage.getItem("contacts"))) {
    if (user["email"] == contact["email"]) {
      user_exsits = true;
    }
  }
  if (user_exsits == false) {
    contacts.push(contact);
    chats.push(chat);
    localStorage.setItem("chats", JSON.stringify(chats));
    localStorage.setItem("contacts", JSON.stringify(contacts));
  }

  // display all users in "Recent"
  Recent = JSON.parse(localStorage.getItem("contacts"));

  console.log("====iterate user====");
  for (new_usr of Recent) {
    let user = `

                <a href="#" class="user" class="list-group-item list-group-item-action list-group-item-light rounded-0" email=${new_usr["email"]}>
                 <div class="media"><img src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg"
                    alt="user" width="50" class="rounded-circle">
                  <div class="media-body ml-4">
                    <div class="d-flex align-items-center justify-content-between">
                    <!--<h6 class="mb-0" class="user_name">
                      ${new_usr["name"]}
                      </h6>-->
                      <h6 class="mb-0" class="user_email">
                      ${new_usr["email"]}
                      </h6>
                          <small class="small font-weight-bold">${new_usr["date"]}</small>
                    </div>
                  </div>
                </div>
              </a>

              `;
    $("#contact-list").append(user);
    scroll_to_bottom();
  }
}

function sendMessage(message, date) {
  let ReMessage = `
            <!-- Reciever Message-->
            <div class="media w-75 ml-auto">
            <div class="media-body">
                <div class="bg-primary rounded py-2 px-3">
                <p class="text-small mb-0 text-white">${message}</p>
                </div>
                <p class="small text-muted">${date}</p>
            </div>
            </div>
    
                `;

  $("#chat-box").append(ReMessage);

  scroll_to_bottom();
}

function receiveMessage(msg, date) {
  let from = msg["src"];
  let message = msg["message"];

  let reMessage = `
                <div class="media w-50 mb-3"><img
                src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg" alt="user" width="50"
                class="rounded-circle">
              <div class="media-body ml-3">
                <div class="bg-light rounded py-2 px-3 mb-2">
                  <p class="text-small mb-0 text-muted">${message}</p>
                </div>
                <p class="small text-muted">${date}</p>
              </div>
              </div> 
  `;
  $("#chat-box").append(reMessage);

  scroll_to_bottom();
}

function switch_Users_chatbox(to) {
  let chats = JSON.parse(localStorage.getItem("chats"));
  console.log("load history");
  for (user_chat of chats) {
    if (user_chat["to"] == to) {
      // console.log(to);
      // console.log(user_chat["to"]);
      for (messages of user_chat["chat_function"]) {
        if (messages["src"] == to) {
          console.log(messages);
          receiveMessage(messages, messages["date"]);
          console.log("receive messages");
          console.log(messages);
        } else {
          sendMessage(messages["message"], messages["date"]);
          console.log("send messages");
          console.log(messages["message"]);
        }
      }
    }
  }
}
