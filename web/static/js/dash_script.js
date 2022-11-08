
let device = 'all'

function myFunction(msg, dest) {

    chatSocket.send(JSON.stringify({
        'message': msg,
        'username': 'web',
        'destination': dest,
    }));
}
function myFunction2(msg) {
    console.log(device)
    chatSocket.send(JSON.stringify({
        'message': msg,
        'username': 'web',
        'destination': device,
    }));
}

const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/' +
    'term' +
    '/'
);

function testMsg(msg) {
    console.log(msg)
    device = msg
    let label = document.getElementById("device");
    label.innerHTML = "Selected Device: " + device

}
function getDevices() {
    myFunction('devices', 'web');

}


chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data)
    if (data.destination == 'web' || data.destination == 'all') {
        if (data.message.includes('all')) {
            let list = document.getElementById("list");
            while (list.firstChild) {
                list.removeChild(list.firstChild);
            }
            for (let i = 0; i < data.message.length; i++) {
                console.log(data.message[i])
                if (data.message[i] != 'web') {
                    var button = document.createElement("button");
                    button.innerHTML = data.message[i];
                    button.onclick = function () { testMsg(data.message[i]); }
                    list.appendChild(button);
                }
            }
        }
    }
}