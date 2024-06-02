<template>
  <div class="chart-container">
    <Bar
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: ['ducking', 'vest'],
  computed: {
    chartData() {
      const totalDucking = this.ducking.length;
      const totalVest = this.vest.length;

      return {
        labels: ['Нарушения'],
        datasets: [
          {
            label: 'Опасность у поезда',
            backgroundColor: '#e21a1a',
            data: [totalDucking],
          },
          {
            label: 'Отсутсвие СИЗ',
            backgroundColor: '#d9802e',
            data: [totalVest],
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        },
        barThickness: "25",
      };
    },
  }
}
</script>

<style>
.chart-container {
  display: flex;
  justify-content: center;
  padding: 15rem;
}
</style>