
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
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.destination == 'web' || data.destination == 'all') {
        console.log(data)
    }
}