<template>
  <div class="player-page">
    <video
      v-if="videoSrc"
      ref="videoPlayer"
      controls
    >
      <source :src="videoSrc" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div v-else class="loader" style="margin-bottom: 3rem;"></div>
    <h5 class="va-h5">
      <VaIcon name="play_arrow" style="margin-right: 0.5rem;"/>
      доступные видео:
    </h5>
    <div v-for="(url, index) in videoUrls" :key="index">
      <VaButton
        color="#e21a1a"
        preset="secondary"
        @click="fetchVideo(url)"
        style="gap: 0.8rem;"
      >
        <VaIcon name="link" style="margin-right: 0.5rem;"/>
        {{ url }}
      </VaButton>
    </div>
    <h5 class="va-h5">
      <VaIcon name="warning" style="margin-right: 0.5rem;"/>
      выявленные нарушения:
    </h5>
    <div style="display: flex; justify-content: space-between;">
      <div class="timestamp-container" v-for="(time, index) in ducking" :key="'ducking-' + index" style="color: red;">
        <VaButton color="#e21a1a" preset="secondary" border-color="#e21a1a" @click="seekToTime(time)" style="margin-right: 0.5rem;"><VaIcon name="train" />Опасность у поезда, {{ convertSecondsToString(time) }}</VaButton>
      </div>
      <div class="timestamp-container" v-for="(time, index) in vest" :key="'vest-' + index" style="color: blue;">
        <VaButton color="#d9802e" preset="secondary" border-color="#d9802e" @click="seekToTime(time)" style="margin-right: 0.5rem;"><VaIcon name="engineering" />Отсутствие СИЗ, {{ convertSecondsToString(time) }}</VaButton>
      </div>
    </div>
  </div>
  <BarChart :ducking="ducking" :vest="vest" />
</template>

<script>
import axios from 'axios';
import BarChart from './BarChart.vue';

export default {
  name: 'PlayerPage',
  data() {
    return {
      ducking: [],
      vest: [],
      videoSrc: null,
      videoUrls: [],
    };
  },
  mounted() {
    this.fetchVideoUrls();
  },
  methods: {
    convertSecondsToString(seconds) {
      const minutes = Math.floor(seconds / 60);
      const remainingSeconds = seconds % 60;
      return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
    },
    async fetchVideoUrls() {
      try {
        const response = await axios.get('http://192.168.110.63:3000/getvideos', { responseType: 'json' });
        this.videoUrls = response.data.files;
        console.log(this.videoUrls);
      } catch (error) {
        console.error('Error fetching video data:', error);
      }
    },
    async fetchVideo(name) {
      try {
        const videoResponse = await axios.get(`http://192.168.110.63:3000/getvideo/${name}`, { responseType: 'blob' });
        const videoBlob = new Blob([videoResponse.data], { type: 'video/mp4' });
        this.videoSrc = URL.createObjectURL(videoBlob);

        const violationResponse = await axios.get(`http://192.168.110.63:3000/getviolation/${name}`);
        const violationData = violationResponse.data;

        this.ducking = violationData.ducking;
        this.vest = violationData.vest;

        console.log(violationData);
      } catch (error) {
        console.error('Error fetching video or violation data:', error);
      }
    },
    seekToTime(timeString) {
      const totalSeconds = parseInt(timeString, 10);
      const formattedTimeString = this.convertSecondsToString(totalSeconds);
      this.$refs.videoPlayer.currentTime = totalSeconds;
      console.log(formattedTimeString);
    },
    convertSecondsToString(seconds) {
      let hours = Math.floor(seconds / 3600);
      let minutes = Math.floor((seconds % 3600) / 60);
      let remainingSeconds = seconds % 60;

      hours = hours < 10? '0' + hours : hours;
      minutes = minutes < 10? '0' + minutes : minutes;
      remainingSeconds = remainingSeconds < 10? '0' + remainingSeconds : remainingSeconds;

      return `${hours}:${minutes}:${remainingSeconds}`;
    },
  },
  components: {
    BarChart,
  },
};
</script>
  
<style scoped>
.player-page {
  text-align: center;
  display: flex;
  justify-content:center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100vh;
}

video {
  width: auto;
  height: 65%;
  border-radius: 10px;
  border: #e21a1a 1px solid;
}

.loader {
  width: 200px;
  height: 30px;
  border-radius: 20px;
  background:
    repeating-linear-gradient(135deg,#f03355 0 10px,#ffa516 0 20px) 0/0%   no-repeat,
    repeating-linear-gradient(135deg,#ddd    0 10px,#eee    0 20px) 0/100%;
  animation: l3 2s infinite;
}
  
@keyframes l3 {
  100% {background-size:100%}
}

.timestamp-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
</style>