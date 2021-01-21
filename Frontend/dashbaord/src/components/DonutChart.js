import React, { useEffect, useState } from "react";
import { Chart as ChartFunc } from "chart.js";
import axios from "axios";

ChartFunc.defaults.global.responsive = true;
ChartFunc.defaults.global.maintainAspectRatio = false;

const OsChart = (props) => {
  let [Data, setData] = useState({ data: [], labels: [] });

  useEffect(() => {
    const url = props.url + props.shortcode;
    axios.get(url).then((response) => setData(response.data));
  }, [props.url, props.shortcode]);

  useEffect(() => {
    console.log(props.id);
    const ctx = document.getElementById(props.id);
    new ChartFunc(ctx, {
      type: "doughnut",
      data: {
        labels: Data.labels,
        datasets: [
          {
            label: "# of Votes",
            data: Data.data.length === 0 ? [0] : Data.data,
            backgroundColor: [
              "rgb(54, 162, 235)",
              "rgb(255, 205, 86)",
              "rgb(153, 102, 255)",
              "rgb(255, 99, 132)",
              "rgb(255, 159, 64)",
              "rgb(75, 192, 192)",
              "rgb(201, 203, 207)",
            ],
            borderColor: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "top",
          },
          title: {
            display: true,
            text: "Top Countries",
          },
        },
        animation: {
          animateScale: true,
          animateRotate: true,
        },
      },
    });
  }, [Data]);

  return (
    <React.Fragment>
      <canvas id={props.id} width="1" height="1" />
    </React.Fragment>
  );
};

export default OsChart;
