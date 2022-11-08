
let device = 'all'

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



chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.destination == 'web' || data.destination == 'all') {
        console.log(data)
        if (data.message.includes('mon:false')) {
            let label = document.getElementById("monStat");
            label.innerHTML = "Mon: Off";
        }
        else if (data.message.includes('mon:true')) {
            let label = document.getElementById("monStat");
            label.innerHTML = "Mon: On";
        }
    }
}