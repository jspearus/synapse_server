import React, { Component } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";
import useWebSocket from 'react-use-websocket';

import './App.css';


const WS_URL = 'ws://192.168.1.20:8000/ws/term/';

const chatSocket = new WebSocket(WS_URL);


function sendMsg(msg, dest) {
  chatSocket.send(JSON.stringify({
    'message': msg,
    'username': 'web',
    'destination': dest,
  }));

}

function sendClicked() {
  sendMsg('clicked', 'red')
}

chatSocket.onmessage = function (event) {
  const json = JSON.parse(event.data);
  try {
    if ((json.destination === "red")) {

      console.log(`[message] Data received from server: ${json.username}`);
      console.log(json.message);
    }
  } catch (err) {
    console.log(err);
  }

};


function App() {
  chatSocket.onopen = (event) => {
    sendMsg('hello', 'red')
  };

  return (
    <>
      <h1>Red Thumb Dashboard</h1>
      <button onClick={sendClicked}>click</button>
    </>
  );
}

export default App;