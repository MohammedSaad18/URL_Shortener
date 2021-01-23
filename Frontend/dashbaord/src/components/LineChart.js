import React, { useEffect, useState } from "react";
import { Chart as ChartFunc } from "chart.js";
import { Line } from "react-chartjs-2";

import axios from "axios";

ChartFunc.defaults.global.responsive = true;
ChartFunc.defaults.global.maintainAspectRatio = false;

const LineChart = (props) => {
  let [Data, setData] = useState({ data: [], labels: [] });

  useEffect(() => {
    const url = `http://localhost:8000/api/lineplot/${props.shortcode}`;
    axios.get(url).then((response) => setData(response.data));
  }, [props.shortcode]);

  // useEffect(() => {
  //   const ctx = document.getElementById("myChart");
  //   new ChartFunc(ctx, {
  //     type: "line",
  //     data: {
  //       labels: Data.labels,
  //       datasets: [
  //         {
  //           label: "# of Vistis",
  //           data: Data.data,
  //           backgroundColor: ["rgba(237, 86, 128,0.2)"],
  //           borderColor: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
  //           borderWidth: 1,
  //         },
  //       ],
  //     },
  //     options: {
  //       scales: {
  //         xAxes: [
  //           {
  //             gridLines: {
  //               drawOnChartArea: false,
  //             },
  //           },
  //         ],
  //         yAxes: [
  //           {
  //             gridLines: {
  //               drawOnChartArea: false,
  //             },
  //             ticks: {
  //               beginAtZero: true,
  //             },
  //           },
  //         ],
  //       },
  //     },
  //   });
  // }, [Data]);

  const getData = () => {
    return {
      labels: Data.labels,
      datasets: [
        {
          label: "# of Vistis",
          data: Data.data,
          backgroundColor: ["rgba(237, 86, 128,0.2)"],
          borderColor: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
          borderWidth: 1,
        },
      ],
    };
  };

  const getOptions = {
    scales: {
      xAxes: [
        {
          gridLines: {
            drawOnChartArea: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            drawOnChartArea: false,
          },
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  };

  return <Line data={getData} options={getOptions} />;
};

export default LineChart;
