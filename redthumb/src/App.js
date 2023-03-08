import React, { Component } from 'react';
import { Card, CardContent, Box, CssBaseline, Typography } from '@mui/material';
import { Colors } from "./styles/colors";

import './App.css';


const WS_URL = 'ws://192.168.1.20:8000/ws/term/';

const chatSocket = new WebSocket(WS_URL);


function sendMsg(msg, dest) {
  chatSocket.send(JSON.stringify({
    'message': msg,
    'username': 'red',
    'destination': dest,
  }));

}

function sendClicked() {
  sendMsg('status', 'plants')
}

chatSocket.onmessage = function (event) {
  const json = JSON.parse(event.data);
  try {
    if (json.destination === "red" || json.destination === "web") {

      // console.log(`[message] Data received from server: ${json.username}`);
      console.log(json.message);
      if (json.message.includes('mlevels')) {
        const lvls = json.message.split(",");
        let label = document.getElementById("status");
        label.innerHTML = "plant1 Level- " + lvls[1] + " plant2 Level- " + lvls[2] + " plant3 Level- " + lvls[3];
      }
      else if (json.message.includes('tanklvl')) {
        const lvl = json.message.split(":");
        let label = document.getElementById("tanklvl");
        label.innerHTML = "Tank Level - " + lvl[1];
      }
    }
  } catch (err) {
    console.log(err);
  }

};


function App() {
  chatSocket.onopen = (event) => {
    sendMsg('status', 'plants')
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column' }}>
      <CssBaseline />
      <Card sx={{ my: 10, mx: 10, width: "75%" }}>
        <CardContent>
          <Typography
            variant='h4'
            sx={{ color: Colors.primary }}>Red Thumb</Typography>
          <Typography id='status'> </Typography>
          <Typography id='tanklvl'> </Typography>
        </CardContent>
      </Card>
    </Box>
  );
}

export default App;