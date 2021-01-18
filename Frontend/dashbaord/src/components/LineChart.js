import React, { useEffect, useState } from "react";
import { Chart as ChartFunc } from "chart.js";
import axios from "axios";

ChartFunc.defaults.global.responsive = true;
ChartFunc.defaults.global.maintainAspectRatio = false;

const LineChart = (props) => {
  let [Data, setData] = useState({ data: [], labels: [] });

  useEffect(() => {
    const url = `http://localhost:8000/api/lineplot/${props.shortcode}`;
    axios.get(url).then((response) => setData(response.data));
  }, [props.shortcode]);

  useEffect(() => {
    const ctx = document.getElementById("myChart");
    new ChartFunc(ctx, {
      type: "line",
      data: {
        labels: Data.labels,
        datasets: [
          {
            label: "# of Votes",
            data: Data.data,
            backgroundColor: ["white"],
            borderColor: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
            borderWidth: 1,
          },
        ],
      },
    });
  }, [Data]);

  return (
    <React.Fragment>
      <canvas id="myChart" width="1" height="1" />
    </React.Fragment>
  );
};

export default LineChart;
