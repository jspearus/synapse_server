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
    if (data.destination == 'web' || data.destination == 'remote') {
        console.log(data)
        if (data.message.includes('remauto:true')) {
            let label = document.getElementById("auto");
            label.innerHTML = "Auto: On";
        }
        else if (data.message.includes('remauto:false')) {
            let label = document.getElementById("auto");
            label.innerHTML = "Auto: Off";
        }
        else if (data.message.includes('remnextevent')) {
            let label = document.getElementById("event");
            let nextEvent = data.message.split(":");
            label.innerHTML = "Next Event: " + nextEvent[1] + " : " + nextEvent[2];
        }
        else if (data.message.includes('remcomm')) {
            let label = document.getElementById("command");
            let nextEvent = data.message.split(":");
            label.innerHTML = "Pre Command: " + nextEvent[1];
        }

    }

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