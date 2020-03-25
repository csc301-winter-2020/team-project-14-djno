$(document).ready(function() {
  // let contacts = [];
  // let messages = [];

  // // add sample users and messages into test
  // user1 = {
  //   name: "Jason Doe",
  //   email: "123@gmail.com",
  //   date: date()
  // };

  // user2 = {
  //   name: "Jane Tim",
  //   email: "345@gmail.com",
  //   date: date()
  // };

  // message1 = {
  //   re_email: "me@gmail.com",
  //   se_email: "123@gmail.com",
  //   messages: [
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       se_email: "123@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     }
  //   ]
  // };

  // message2 = {
  //   re_email: "me@gmail.com",
  //   se_email: "345@gmail.com",
  //   messages: [
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     },
  //     {
  //       re_email: "me@gmail.com",
  //       message: "hello",
  //       time: date()
  //     }
  //   ]
  // };

  // //update contact list
  // contacts.push(user1);
  // localStorage.setItem("contacts", JSON.stringify(contacts));
  // $("#contact-list").append(newUser());
  // messages.push(message1);
  // localStorage.setItem("messages", JSON.stringify(contacts));

  // contacts.push(user2);
  // localStorage.setItem("contacts", JSON.stringify(contacts));
  // $("#contact-list").append(newUser());
  // messages.push(message2);
  // localStorage.setItem("messages", JSON.stringify(contacts));

  // // switch user message interface
  // $(".user").click(function() {
  //   console.log("switch user");
  //   // let switch_user_email = ($(this)
  //   //   .find(".user_email"))
  //   //   .val();
  //   //   console.log(switch_user_email)
  //   $("#chat-box").empty();
  //   // $("#chat-box").loadPreviousMessage(switch_user);
  //   $("#type-message").val("");
  // });

  let is_connected = false;
  var socket = io();
  socket.on("chat", function(msg) {
    console.log("message is....");
    console.log(msg);
    // //reveice message
    // receiveMessage(msg)
  });
  socket.on("connect", function() {
    socket.emit("join", {
      email: "weiyi.henry.hu@gmail.com",
      target: "weiyi.henry.hu@gmail.com",
      message: "connect"
    });
    console.log("emitted!");
  });
  socket.on("joined", function(msg) {
    console.log("joined");
    console.log(msg);
    //send message
    $("#Message-send-button").click(function() {
      $("#chat-box").append(sendMessage());
      socket.emit("chat", {
        email: "weiyi.henry.hu@gmail.com",
        target: "weiyi.henry.hu@gmail.com",
        message: $("#type-message").val()
      });
    });
  });

  socket.on("failed", function(msg) {
    console.log("failed!");
    console.log(msg);
  });

  // //reveice message
  // receiveMessage()
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

// function newUser() {
//   new_user = JSON.parse(localStorage.getItem("contacts")).slice(-1)[0];
//   let user = `

//                 <a href="#" class="user" class="list-group-item list-group-item-action list-group-item-light rounded-0">
//                  <div class="media"><img src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg"
//                     alt="user" width="50" class="rounded-circle">
//                   <div class="media-body ml-4">
//                     <div class="d-flex align-items-center justify-content-between mb-3">
//                       <h6 class="mb-0" class="user_name">
//                       ${new_user["name"]}
//                       </h6>
//                       <h6 class="mb-0" class="user_email">
//                       ${new_user["email"]}
//                       </h6>
//                           <small class="small font-weight-bold">${new_user["date"]}</small>
//                     </div>
//                   </div>
//                 </div>
//               </a>

//               `;

//   return user;
// }

function sendMessage() {
  if ($("#type-message").val()) {
    const message = $("#type-message").val();

    let ReMessage = `
            <!-- Reciever Message-->
            <div class="media w-50 ml-auto mb-3">
            <div class="media-body">
                <div class="bg-primary rounded py-2 px-3 mb-2">
                <p class="text-small mb-0 text-white">${message}</p>
                </div>
                <p class="small text-muted">${date()}</p>
            </div>
            </div>
    
                `;

    return ReMessage;
  }
}

// function loadPreviousMessage() {

// }
