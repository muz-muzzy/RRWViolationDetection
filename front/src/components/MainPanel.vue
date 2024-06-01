<template>
  <div class="main-panel-container">
    <h1 class="va-h1">Анализ видео на предмет нарушения техники безопасности👷‍♂️</h1>
    <h2 class="va-h3" style="z-index: 10;">Загрузите видео в формате <span style="font-style: italic;">mp4</span></h2>

    <VaFileUpload
      v-model="uploader"
      dropzone
      type="list"
      dropZoneText="Перетащите видео сюда"
      uploadButtonText="Загрузить"
      color="#e63c3c"
    />
    <VaButton @click="startUpload" :loading="isLoading" size="large" color="#e21a1a"> 
       Отправить видео <VaIcon name="send" style="margin-left: 0.5rem;"/>
    </VaButton>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      uploader: [],
      isLoading: false,
    };
  },
  methods: {
    async startUpload() {
      this.isLoading = true;
      const file = this.uploader[0];
      if (!file) return;  
      try {
        const formData = new FormData();
        formData.append('file', file);

        await axios.post('http://192.168.110.63:3000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('File uploaded successfully');
        this.isLoading = false;
      } catch (error) {
        console.error('Failed to upload file:', error);
      } finally {
        this.isLoading = false;
      }
    },
  },
  name: 'MainPanel',
}
</script>

<style>
.main-panel-container {
  justify-content: center;
  padding-bottom: 6rem;
  padding-left: 20rem;
  padding-right: 20rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  height: 100vh;
}
</style>
