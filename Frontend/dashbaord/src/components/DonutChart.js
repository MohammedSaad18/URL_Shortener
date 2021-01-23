import React, { useEffect, useState } from "react";
import axios from "axios";
import { Doughnut } from 'react-chartjs-2';


const colors = [
  "rgb(54, 162, 235)",
  "rgb(75, 192, 192)",
  "rgb(255, 205, 86)",
  "rgb(153, 102, 255)",
  "rgb(255, 99, 132)",
  "rgb(255, 159, 64)",
  "rgb(201, 203, 207)",
  '#36A2EB',
  '#FF6384',
  '#FFCE56',
  ]

const Chart = (props) => {
  let [Data, setData] = useState({ data: [], labels: [] });

  useEffect(() => {
    const url = props.url + props.shortcode;
    axios.get(url).then((response) => setData(response.data));
  }, [props.url, props.shortcode]);

  const getData = () => {
    return {
      labels: Data.labels,
      datasets: [{
        data: Data.data,
        backgroundColor: colors,
        hoverBackgroundColor: colors
      }]
    }
  }
  
  return (
    <Doughnut 
      data = {getData}
    />
  );
};

export default Chart;
