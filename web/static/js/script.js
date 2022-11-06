const user_username = JSON.parse(document.getElementById('user_username').textContent);
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const node = document.getElementsByClassName("container")[0];

node.addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        const messageInputDom = document.querySelector('#input');
        const message = messageInputDom.value;

        const destInputDom = document.querySelector('#dest');
        const dest = destInputDom.value;

        chatSocket.send(JSON.stringify({
            'message': message,
            'username': 'web',
            'destination': dest,
        }));
        messageInputDom.value = '';
        //destInputDom.value = '';
        messageInputDom.setSelectionRange(0, 0);
        messageInputDom.focus();
    }
});

document.querySelector('#submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;

    const destInputDom = document.querySelector('#dest');
    const dest = destInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': 'web',
        'destination': dest,
    }));
    messageInputDom.value = '';
    //destInputDom.value = '';
    messageInputDom.setSelectionRange(0, 0);
    messageInputDom.focus();

};
document.querySelector('#button').onclick = function (e) {
    document.querySelector('#button').setAttribute("disabled", "");
};

const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/' +
    roomName +
    '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data)
    if (data.destination == 'web' || data.destination == 'all') {
        document.querySelector('#alert').innerHTML = (data.username + ': Sent -  ' + data.message + '\n')
        if (data.message == 'test') {
            document.querySelector('#button').removeAttribute("hidden");
            document.querySelector('#button').innerHTML = ("succses")
        }
    }
    document.querySelector('#chat-text').value += (data.username + ': ' + data.message + '\n')
}