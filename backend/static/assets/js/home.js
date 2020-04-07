$(document).ready(async function () {
    /* Change DOM content */
    // First name
    document.querySelectorAll("#profile-first-name").forEach(first_name => {
        first_name.innerText = localStorage.getItem("first_name");
    });
});

/* Functions */
function declineRequest(button) {
    button.offsetParent.offsetParent.remove();
    console.log("TODO: send declineRequest to server");
}

function chat(button) {
    let email = button.getAttribute("email");
    let name = button.getAttribute("name");
    localStorage.setItem("to", JSON.stringify({email: email, name: name}));
    location.replace("/chat.html");

    // button.offsetParent.remove();
    console.log("TODO: chat with profile user");
}

function updateSetting(selectObj) {
    const key = selectObj.name;
    const returnObj = {};
    returnObj["email"] = localStorage.getItem("email");

    // Currently we only allow update a pair of key
    returnObj[key] = $(selectObj).val();

    console.log(`Updating ${key} to ${returnObj[key]}`);

    console.log(returnObj);

    return $.ajax({
        type: "POST",
        url: "/users/settings",

        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(returnObj),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: data => {
            console.log(`Update setting: ${data.update_a_user_settings_success}`);
        },
        failure: function (errMsg) {
            console.log(`Update setting failed: ${errMsg}`);
        }
    });
}

function preloadSetting(user_setting) {
    // Preload not necessary if user has never changed setting before.
    if (user_setting[this.name] === undefined) {
        console.error(`${this.name} is not in ${user_setting}`);
        return;
    }

    for (let i = 0; i < this.options.length; i++) {
        if (user_setting[this.name].includes(this.options[i].value)) {
            this.options[i].selected = true;
        }
    }
}

function makeNewRequest() {
    let location = [0, 0];
    let options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };

    new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            pos => {
                let crd = pos.coords;
                resolve([crd.longitude, crd.latitude]);
            },
            err => {
                resolve(location);
            },
            options
        );
    }).then(cur_location => {
        let validSave = true;

        document
            .querySelectorAll(
                "[name=title], [name=location], [type=datetime-local], #request-type, [name=message]"
            )
            .forEach(field => {
                // Reset invalid style
                field.classList.remove("invalid");

                if (
                    field.value.length === 0 ||
                    field.value === "2020-01-01T00:00" ||
                    field.value === "0"
                ) {
                    console.log(field);
                    console.log("is invalid");
                    validSave = false;
                    field.classList.add("invalid");
                }
            });

        if (validSave) {
            // let title = document.querySelector("[name=title]").value;
            let location = document.querySelector("[name=location]").value;
            // let datetime = document.querySelector("[type=datetime-local]").value;
            let requestType = document.querySelector("#request-type").value;
            // let message = document.querySelector("[name=message]").value;

            let returnObj = {
                email: localStorage.getItem("email"),
                request_type: requestType,
                // "title": title,
                location: cur_location
                // "datetime": datetime,
                // "message": message
            };
            console.log("location is: ....");
            console.log(returnObj);

            // Hide make request modal.
            $("#modal-2").modal("hide");

            $.ajax({
                type: "POST",
                url: "/match",

                // The key needs to match your method's input parameter (case-sensitive).
                data: JSON.stringify(returnObj),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: async data => {
                    // Change greeting
                    document.querySelector("#greetingMessage").innerText =
                        ", You got a matching result!";
                    document.querySelector("#greetingDetail").innerText =
                        "These people beings might be able to help you!";

                    // List of matching profiles up to top 10 results.
                    const e = document.createElement("div");
                    e.classList.add("matching_list");

                    // Appending the list of matching profiles.
                    for (let i = 0; i < data.length && i < 9; i++) {
                        // Receive matching profile
                        let result = await get_user_profile(data[i]["email"]);
                        let profile = result.profile;
                        let name = profile["first_name"] + " " + profile["last_name"][0]; //only show the first character in last name
                        let profilePic = profile["image_url"];
                        let email = data[i]["email"];

                        // Profile picture placeholder
                        if (profilePic == null) {
                            let gender = profile["gender"];

                            if (gender === "Male") {
                                profilePic = "/assets/img/male-user-profile-picture.svg";
                            } else if (gender === "Female") {
                                profilePic = "/assets/img/female-user-profile-picture.svg";
                            } else {
                                profilePic = "/assets/img/neutral-user-profile-picture.svg";
                            }
                        }

                        console.log(`Matching with : ${name} - ${data[i]["email"]}`);

                        // Adding one matching profile.
                        e.innerHTML +=
                            '<div class="matching">\n' +
                            '            <div class="border rounded matching-back"><button class="btn btn-primary d-xl-flex align-items-xl-center btn-success" type="button"><i class="material-icons">sentiment_very_satisfied</i>Chat</button><button class="btn btn-primary btn-danger" type="button">Dismiss</button></div>\n' +
                            '            <div class="text-center border rounded shadow-sm profile-box matching-front">\n' +
                            '                <div class="decoration"></div>\n' +
                            '                <div><img class="rounded-circle" src="' +
                            profilePic +
                            '" width="60px" height="60px"></div>\n' +
                            '                <div class="profile-info">\n' +
                            "                    <h4>" +
                            name +
                            "</h4>\n" +
                            "                </div>\n" +
                            '                <div class="text-center" id="profile-buttons"><button class="btn btn-success btn-sm" id="chat-request" type="button" onclick="chat(this)" name=' +
                            name +
                            " email=" +
                            email +
                            '>Chat</button><button class="btn btn-danger btn-sm" id="decline-request" type="button" onclick="declineRequest(this);">Dismiss</button></div>\n' +
                            "        </div>\n" +
                            "        </div>";
                    }

                    // Finally append the matching profile list
                    document.querySelector("main").appendChild(e);

                    // Activate swipe event on all matching blocks
                    swipeEvent();
                },
                failure: function (errMsg) {
                    console.log(`Update setting failed: ${errMsg}`);
                }
            });
        }
    });
    // let validSave = true;

    // document
    //   .querySelectorAll(
    //     "[name=title], [name=location], [type=datetime-local], #request-type, [name=message]"
    //   )
    //   .forEach(field => {
    //     // Reset invalid style
    //     field.classList.remove("invalid");

    //     if (
    //       field.value.length === 0 ||
    //       field.value === "2020-01-01T00:00" ||
    //       field.value === "0"
    //     ) {
    //       console.log(field);
    //       console.log("is invalid");
    //       validSave = false;
    //       field.classList.add("invalid");
    //     }
    //   });

    // if (validSave) {
    //   // let title = document.querySelector("[name=title]").value;
    //   let location = document.querySelector("[name=location]").value;
    //   // let datetime = document.querySelector("[type=datetime-local]").value;
    //   let requestType = document.querySelector("#request-type").value;
    //   // let message = document.querySelector("[name=message]").value;

    //   let returnObj = {
    //     email: localStorage.getItem("email"),
    //     request_type: requestType,
    //     // "title": title,
    //     location: [1, 2]
    //     // "datetime": datetime,
    //     // "message": message
    //   };
    //   console.log("location is: ....");
    //   console.log(returnObj);

    //   // Hide make request modal.
    //   $("#modal-2").modal("hide");

    //   $.ajax({
    //     type: "POST",
    //     url: "/match",

    //     // The key needs to match your method's input parameter (case-sensitive).
    //     data: JSON.stringify(returnObj),
    //     contentType: "application/json; charset=utf-8",
    //     dataType: "json",
    //     success: async data => {
    //       // Change greeting
    //       document.querySelector("#greetingMessage").innerText =
    //         ", You got a matching result!";
    //       document.querySelector("#greetingDetail").innerText =
    //         "These people beings might be able to help you!";

    //       // List of matching profiles up to top 10 results.
    //       const e = document.createElement("div");
    //       e.classList.add("matching_list");

    //       // Appending the list of matching profiles.
    //       for (let i = 0; i < data.length && i < 9; i++) {
    //         // Receive matching profile
    //         let result = await get_user_profile(data[i]["email"]);
    //         let profile = result.profile;
    //         let name = profile["first_name"] + " " + profile["last_name"][0]; //only show the first character in last name
    //         let profilePic = profile["image_url"];

    //         // Profile picture placeholder
    //         if (profilePic == null) {
    //           let gender = profile["gender"];

    //           if (gender === "Male") {
    //             profilePic = "/assets/img/male-user-profile-picture.svg";
    //           } else if (gender === "Female") {
    //             profilePic = "/assets/img/female-user-profile-picture.svg";
    //           } else {
    //             profilePic = "/assets/img/neutral-user-profile-picture.svg";
    //           }
    //         }

    //         console.log(`Matching with : ${name} - ${data[i]["email"]}`);

    //         // Adding one matching profile.
    //         e.innerHTML +=
    //           '<div class="matching">\n' +
    //           '            <div class="border rounded matching-back"><button class="btn btn-primary d-xl-flex align-items-xl-center btn-success" type="button"><i class="material-icons">sentiment_very_satisfied</i>Chat</button><button class="btn btn-primary btn-danger" type="button">Dismiss</button></div>\n' +
    //           '            <div class="text-center border rounded shadow-sm profile-box matching-front">\n' +
    //           '                <div class="decoration"></div>\n' +
    //           '                <div><img class="rounded-circle" src="' +
    //           profilePic +
    //           '" width="60px" height="60px"></div>\n' +
    //           '                <div class="profile-info">\n' +
    //           "                    <h4>" +
    //           name +
    //           "</h4>\n" +
    //           "                </div>\n" +
    //           '                <div class="text-center" id="profile-buttons"><button class="btn btn-success btn-sm" id="chat-request" type="button" onclick="chat(this)">Chat</button><button class="btn btn-danger btn-sm" id="decline-request" type="button" onclick="declineRequest(this);">Dismiss</button></div>\n' +
    //           "        </div>\n" +
    //           "        </div>";
    //       }

    //       // Finally append the matching profile list
    //       document.querySelector("main").appendChild(e);

    //       // Activate swipe event on all matching blocks
    //       swipeEvent();
    //     },
    //     failure: function(errMsg) {
    //       console.log(`Update setting failed: ${errMsg}`);
    //     }
    //   });
    // }
}

// Retrieve User Profile
function get_user_profile(email) {
    return new Promise((resolve, reject) => {
        $.get(`/users/${email}`, function (data, status) {
            console.log(`Retrieve user profile: ${status}`);
            resolve(data);
        });
    });
}

/******************
 * Below are swipe related
 *****************/

// Shim for requestAnimationFrame from Paul Irishpaul ir
// http://www.paulirish.com/2011/requestanimationframe-for-smart-animating/
window.requestAnimFrame = (function () {
    "use strict";

    return (
        window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        function (callback) {
            window.setTimeout(callback, 1000 / 60);
        }
    );
})();

/* // [START pointereventsupport] */
var pointerDownName = "pointerdown";
var pointerUpName = "pointerup";
var pointerMoveName = "pointermove";

if (window.navigator.msPointerEnabled) {
    pointerDownName = "MSPointerDown";
    pointerUpName = "MSPointerUp";
    pointerMoveName = "MSPointerMove";
}

// Simple way to check if some form of pointerevents is enabled or not

window.PointerEventsSupport = !!(
    window.PointerEvent || window.navigator.msPointerEnabled
);

/* // [END pointereventsupport] */

function SwipeRevealItem(element) {
    "use strict";

    // Gloabl state variables
    var STATE_DEFAULT = 1;
    var STATE_LEFT_SIDE = 2;
    var STATE_RIGHT_SIDE = 3;

    var swipeFrontElement = element.querySelector(".matching-front");
    var rafPending = false;
    var initialTouchPos = null;
    var lastTouchPos = null;
    var currentXPosition = 0;
    var currentState = STATE_DEFAULT;
    var handleSize = -50; // negative val make it disappear on the screen

    // Perform client width here as this can be expensive and doens't
    // change until window.onresize
    var itemWidth = swipeFrontElement.clientWidth;
    var slopValue = itemWidth * (3 / 10);

    // On resize, change the slop value
    this.resize = function () {
        itemWidth = swipeFrontElement.clientWidth;
        slopValue = itemWidth * (3 / 10);
    };

    /* // [START handle-start-gesture] */
    // Handle the start of gestures
    this.handleGestureStart = function (evt) {
        console.log("handleGestureStart");
        evt.preventDefault();

        if (evt.touches && evt.touches.length > 1) {
            return;
        }

        // Add the move and end listeners
        if (window.PointerEvent) {
            evt.target.setPointerCapture(evt.pointerId);
        } else {
            // Add Mouse Listeners
            document.addEventListener("mousemove", this.handleGestureMove, true);
            document.addEventListener("mouseup", this.handleGestureEnd, true);
        }

        initialTouchPos = getGesturePointFromEvent(evt);

        swipeFrontElement.style.transition = "initial";
    }.bind(this);
    /* // [END handle-start-gesture] */

    // Handle move gestures
    //
    /* // [START handle-move] */
    this.handleGestureMove = function (evt) {
        evt.preventDefault();

        if (!initialTouchPos) {
            return;
        }

        lastTouchPos = getGesturePointFromEvent(evt);

        if (rafPending) {
            return;
        }

        rafPending = true;

        window.requestAnimFrame(onAnimFrame);
    }.bind(this);
    /* // [END handle-move] */

    /* // [START handle-end-gesture] */
    // Handle end gestures
    this.handleGestureEnd = function (evt) {
        console.log("handleGestureEnd");
        evt.preventDefault();

        if (evt.touches && evt.touches.length > 0) {
            return;
        }

        rafPending = false;

        // Remove Event Listeners
        if (window.PointerEvent) {
            evt.target.releasePointerCapture(evt.pointerId);
        } else {
            // Remove Mouse Listeners
            document.removeEventListener("mousemove", this.handleGestureMove, true);
            document.removeEventListener("mouseup", this.handleGestureEnd, true);
        }

        updateSwipeRestPosition();

        initialTouchPos = null;
    }.bind(this);

    /* // [END handle-end-gesture] */

    function updateSwipeRestPosition() {
        var differenceInX = initialTouchPos.x - lastTouchPos.x;
        currentXPosition = currentXPosition - differenceInX;

        // Go to the default state and change
        var newState = STATE_DEFAULT;

        // Check if we need to change state to left or right based on slop value
        if (Math.abs(differenceInX) > slopValue) {
            if (currentState === STATE_DEFAULT) {
                if (differenceInX > 0) {
                    newState = STATE_LEFT_SIDE;
                } else {
                    newState = STATE_RIGHT_SIDE;
                }
            } else {
                if (currentState === STATE_LEFT_SIDE && differenceInX > 0) {
                    newState = STATE_DEFAULT;
                } else if (currentState === STATE_RIGHT_SIDE && differenceInX < 0) {
                    newState = STATE_DEFAULT;
                }
            }
        } else {
            newState = currentState;
        }

        changeState(newState);

        swipeFrontElement.style.transition = "all 150ms ease-out";
    }

    function changeState(newState) {
        var transformStyle;
        switch (newState) {
            case STATE_DEFAULT:
                currentXPosition = 0;
                break;

            case STATE_LEFT_SIDE: // Dismiss
                currentXPosition = -(itemWidth - handleSize);
                console.log("dismissed!");

                const target = swipeFrontElement.closest(".matching");

                // Swipe transition
                target.addEventListener("transitionend", () => {
                    console.log("swipe ended");
                    // Height transition
                    target.classList.add("dismiss-animate");
                    target.addEventListener("transitionend", () => {
                        // Finally remove the block
                        console.log("Transition ended... ready to dismiss.");
                        target.remove();
                    });
                });

                break;

            case STATE_RIGHT_SIDE: // Chat
                currentXPosition = itemWidth - handleSize;
                console.log("chat!");

                const target1 = swipeFrontElement.closest(".matching");

                // Swipe transition
                target1.addEventListener("transitionend", () => {
                    console.log("swipe ended");
                    // Height transition
                    target1.classList.add("dismiss-animate");
                    target1.addEventListener("transitionend", () => {
                        // Finally remove the block
                        console.log("Transition ended... ready to dismiss.");
                        target1.remove();
                    });
                });

                break;
        }

        transformStyle = "translateX(" + currentXPosition + "px)";

        swipeFrontElement.style.msTransform = transformStyle;
        swipeFrontElement.style.MozTransform = transformStyle;
        swipeFrontElement.style.webkitTransform = transformStyle;
        swipeFrontElement.style.transform = transformStyle;

        currentState = newState;
    }

    function getGesturePointFromEvent(evt) {
        var point = {};

        if (evt.targetTouches) {
            point.x = evt.targetTouches[0].clientX;
            point.y = evt.targetTouches[0].clientY;
        } else {
            // Either Mouse event or Pointer Event
            point.x = evt.clientX;
            point.y = evt.clientY;
        }

        return point;
    }

    /* // [START on-anim-frame] */
    function onAnimFrame() {
        if (!rafPending) {
            return;
        }
        var differenceInX = initialTouchPos.x - lastTouchPos.x;

        var newXTransform = currentXPosition - differenceInX + "px";
        var transformStyle = "translateX(" + newXTransform + ")";
        swipeFrontElement.style.webkitTransform = transformStyle;
        swipeFrontElement.style.MozTransform = transformStyle;
        swipeFrontElement.style.msTransform = transformStyle;
        swipeFrontElement.style.transform = transformStyle;

        // Swipe to chat
        if (differenceInX > 0) {
            // Match background color with the button color
            swipeFrontElement.parentElement.firstElementChild.style.background =
                "#ff7851";

            // Show the corresponding button
            swipeFrontElement.closest(
                ".matching"
            ).children[0].children[1].style.opacity = 1;

            // Hide the opposite button
            swipeFrontElement.closest(
                ".matching"
            ).children[0].children[0].style.opacity = 0;
        } else {
            // Match background color with the button color
            swipeFrontElement.parentElement.firstElementChild.style.background =
                "#56cc9d";

            // Show the corresponding button
            swipeFrontElement.closest(
                ".matching"
            ).children[0].children[0].style.opacity = 1;

            // Hide the opposite button
            swipeFrontElement.closest(
                ".matching"
            ).children[0].children[1].style.opacity = 0;
        }

        rafPending = false;
    }

    /* // [END on-anim-frame] */

    /* // [START addlisteners] */
    // Check if pointer events are supported.
    if (window.PointerEvent) {
        console.log("hi there");
        // Add Pointer Event Listener
        swipeFrontElement.addEventListener(
            "pointerdown",
            this.handleGestureStart,
            true
        );
        swipeFrontElement.addEventListener(
            "pointermove",
            this.handleGestureMove,
            true
        );
        swipeFrontElement.addEventListener(
            "pointerup",
            this.handleGestureEnd,
            true
        );
        swipeFrontElement.addEventListener(
            "pointercancel",
            this.handleGestureEnd,
            true
        );
    } else {
        console.log("heLLOO there");
        // Add Touch Listener
        swipeFrontElement.addEventListener(
            "touchstart",
            this.handleGestureStart,
            true
        );
        swipeFrontElement.addEventListener(
            "touchmove",
            this.handleGestureMove,
            true
        );
        swipeFrontElement.addEventListener("touchend", this.handleGestureEnd, true);
        swipeFrontElement.addEventListener(
            "touchcancel",
            this.handleGestureEnd,
            true
        );

        // Add Mouse Listener
        swipeFrontElement.addEventListener(
            "mousedown",
            this.handleGestureStart,
            true
        );
    }
    /* // [END addlisteners] */
}

var swipeRevealItems = [];

// Call this to activate swipe event after created elements
function swipeEvent() {
    "use strict";
    var swipeRevealItemElements = document.querySelectorAll(".matching");
    for (var i = 0; i < swipeRevealItemElements.length; i++) {
        swipeRevealItems.push(new SwipeRevealItem(swipeRevealItemElements[i]));
    }

    // We do this so :active pseudo classes are applied.
    window.onload = function () {
        if (/iP(hone|ad)/.test(window.navigator.userAgent)) {
            document.body.addEventListener("touchstart", function () {
            }, false);
        }
    };
}

window.onresize = function () {
    "use strict";
    console.log("User action: window resizing");
    for (let i = 0; i < swipeRevealItems.length; i++) {
        swipeRevealItems[i].resize();
    }
};

var registerInteraction = function () {
    "use strict";
    window.sampleCompleted("index.html-SwipeFrontTouch");
};

var swipeFronts = document.querySelectorAll(".matching-front");
for (let i = 0; i < swipeFronts.length; i++) {
    swipeFronts[i].addEventListener("touchstart", registerInteraction);
}
