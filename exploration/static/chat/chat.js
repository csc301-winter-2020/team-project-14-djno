import Chatkit from '@pusher/chatkit-server'

const tokenProvider = new Chatkit.TokenProvider({
    url: "https://us1.pusherplatform.io/services/chatkit_token_provider/v1/3b0aaedb-1143-4b79-9d00-739eb8d3a067/token"
});
const instanceLocator = "v1:us1:3b0aaedb-1143-4b79-9d00-739eb8d3a067"
const key = "7b8c4c71-e056-45e7-b324-ef9ee7b2098a:wsql6r6lH+07f0CBZWB4+QtA27xZs/JtwvUE+KWPUFk="

//create chatkit
const chatkit = new Chatkit({
    instanceLocator: instanceLocator,
    key: key,
});

//create User
function createUser() {
    chatkit.createUser({
        id: document.getElementById('userCreateID-text').value,
        name: document.getElementById('userCreateName-text').value
    })
    return id, name;
}

//create Room
function createRoom() {
    const chatManager = new Chatkit.ChatManager({
        instanceLocator: instanceLocator,
        userId: createUser().id,
        tokenProvider: tokenProvider
    });

    chatManager
        .connect()
        .then(currentUser => {
            currentUser.subscribeToRoomMultipart({
                roomId: currentUser.rooms[0].id,
                hooks: {
                    onMessage: message => {
                        const ul = document.getElementById("message-list");
                        const li = document.createElement("li");
                        li.appendChild(
                            document.createTextNode(`${message.senderId}: ${
                                // We know our message will have a single part with
                                // a plain text content because we used
                                // sendSimpleMessage. In general we'd have to check
                                // the partType here.
                                message.parts[0].payload.content
                                }`)
                        );
                        ul.appendChild(li);
                    }
                }
            });

            const form = document.getElementById("message-form");
            form.addEventListener("submit", e => {
                e.preventDefault();
                const input = document.getElementById("message-text");
                currentUser.sendSimpleMessage({
                    text: input.value,
                    roomId: currentUser.rooms[0].id
                });
                input.value = "";
            });
        })
        .catch(error => {
            console.error("error:", error);
        })
}




// Delete Room


// Join the room