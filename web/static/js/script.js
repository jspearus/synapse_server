
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
    else if (data.destination == 'foyer') {

        if (data.message.includes('clear')) {
            let label = document.getElementById("weather");
            label.innerHTML = "Condition: Clear";
        }
        else if (data.message.includes('cloud')) {
            let label = document.getElementById("weather");
            label.innerHTML = "Condition: Cloudy";
        }
        else if (data.message.includes('rain')) {
            let label = document.getElementById("weather");
            label.innerHTML = "Condition: Rain";
        }
        else if (data.message.includes('snow')) {
            let label = document.getElementById("weather");
            label.innerHTML = "Condition: Snow";
        }
        else if (data.message.includes('fog')) {
            let label = document.getElementById("weather");
            label.innerHTML = "Condition: Fog";
        }
    }

}