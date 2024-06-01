<template>
  <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
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
            backgroundColor: '#FF6384',
            data: [totalDucking],
          },
          {
            label: 'Отсутсвие СИЗ',
            backgroundColor: '#36A2EB',
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
        }
      };
    }
  }
}
</script>