
let device = 'all'

function myFunction(msg, dest) {

    chatSocket.send(JSON.stringify({
        'message': msg,
        'username': 'web',
        'destination': dest,
    }));
}
function changeColor(box, color) {

    const element = document.getElementById(box);
    element.style.backgroundColor = color;
}
function clearColor(box, color) {
    for (let i = 0; i < box; i++) {
        const element = document.getElementById(i);
        element.style.backgroundColor = color;
    }
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
        else if (data.message.includes('trees:true')) {
            let label = document.getElementById("TreesStat");
            label.innerHTML = "Trees: On";
        }
        else if (data.message.includes('trees:false')) {
            let label = document.getElementById("TreesStat");
            label.innerHTML = "Trees: Off";
        }
        else if (data.message.includes('tree:true')) {
            let label = document.getElementById("tree_status");
            label.innerHTML = "Tree: On";
        }
        else if (data.message.includes('tree:false')) {
            let label = document.getElementById("tree_status");
            label.innerHTML = "Tree: Off";
        }
        else if (data.message.includes('vil:false')) {
            let label = document.getElementById("village_status");
            label.innerHTML = "Village: Off";
        }
        else if (data.message.includes('vil:true')) {
            let label = document.getElementById("village_status");
            label.innerHTML = "Village: On";
        }
        else if (data.message.includes('lights:true')) {
            let label = document.getElementById("LightStat");
            label.innerHTML = "Lights: On";
        }
        else if (data.message.includes('lights:false')) {
            let label = document.getElementById("LightStat");
            label.innerHTML = "Lights: Off";
        }
        else if (data.message.includes('cauto:true')) {
            let label = document.getElementById("auto");
            label.innerHTML = "Auto: On";
        }
        else if (data.message.includes('cauto:false')) {
            let label = document.getElementById("auto");
            label.innerHTML = "Auto: Off";
        }
        else if (data.message.includes('tauto:true')) {
            let label = document.getElementById("TreeAuto");
            label.innerHTML = "Auto: On";
        }
        else if (data.message.includes('tauto:false')) {
            let label = document.getElementById("TreeAuto");
            label.innerHTML = "Auto: Off";
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