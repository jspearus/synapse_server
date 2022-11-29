function myFunction(msg, dest) {

    chatSocket.send(JSON.stringify({
        'message': msg,
        'username': 'web',
        'destination': dest,
    }));
}


const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/' +
    'term' +
    '/'
);