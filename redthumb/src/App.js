import React, { Component, useEffect, setState } from 'react';
import { Card, CardContent, Box, CssBaseline, Typography } from '@mui/material';
import { Colors } from "./styles/colors";
import Chart from 'react-apexcharts'
import * as ReactDOM from 'react-dom/client';

import './App.css';


const WS_URL = 'ws://192.168.1.20:8000/ws/term/';

const chatSocket = new WebSocket(WS_URL);

let numRecords = 1
let time = []
let value = []

const state = {
  options: {
    chart: {
      id: "basic-bar"
    },
    xaxis: {
      categories: time
    },
    stroke: {
      curve: 'smooth',
    }
  },
  series: [
    {
      name: "series-1",
      data: value
    }
  ]
};


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
let chart = null

chatSocket.onmessage = function (event) {
  const json = JSON.parse(event.data);


  try {
    if (json.destination === "red" || json.destination === "web") {

      // console.log(`[message] Data received from server: ${json.username}`);
      console.log(json.message);
      if (json.message.includes('mlevels')) {
        const lvls = json.message.split(",");
        let label = document.getElementById("level");
        label.innerHTML = "Water Sat.- " + lvls[1] + "%";
        value.push(lvls[1]);
        time.push(numRecords);
        numRecords++
        console.log(value)
        console.log(time)
        state.options.xaxis.categories = time;
        state.series.data = value

        if (!chart) {
          const element = (
            <Chart id='chart'
              options={state.options}
              series={state.series}
              type="line"
              width="250"
              height="200"
            />
          );
          const chart = ReactDOM.createRoot(
            document.getElementById('chart')
          );
          chart.render(element);
        }

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
      <Card sx={{ my: 10, mx: 1, mr: 20, width: "100%" }}>
        <CardContent>
          <Typography
            variant='h4'
            sx={{ color: Colors.primary }}>Red Thumb</Typography>
          <Typography id='plantName'>Plant 1</Typography>
          <Typography id='level'> </Typography>
          <Typography id='tanklvl'> </Typography>
          <Chart id='chart'
            options={state.options}
            series={state.series}
            type="line"
            width="250"
            height="200"
          />
        </CardContent>
      </Card>
    </Box>
  );
}

export default App;