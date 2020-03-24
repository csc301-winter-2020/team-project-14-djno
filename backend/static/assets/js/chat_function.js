$(document).ready(function() {
  let contacts = [];
  // add sample users into test
  user1 = {
    name: "Jason Doe",
    email: "123@gmail.com",
    date: date()
  };
  contacts.push(user1);

  localStorage.setItem("contacts", JSON.stringify(contacts));
  $("#contact-list").append(newUser());
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
  new_user = JSON.parse(localStorage.getItem("contacts")).slice(-1)[0];
  let user = `


                <a href="#" class="list-group-item list-group-item-action list-group-item-light rounded-0">
                 <div class="media"><img src="https://res.cloudinary.com/mhmd/image/upload/v1564960395/avatar_usae7z.svg"
                    alt="user" width="50" class="rounded-circle">
                  <div class="media-body ml-4">
                    <div class="d-flex align-items-center justify-content-between mb-3">
                      <h6 class="mb-0">
                      ${new_user["name"]}
                      </h6>
                          <small class="small font-weight-bold">${new_user["date"]}</small>
                    </div>
                  </div>
                </div>
              </a>
              
              
              
              `;

  return user;
}
