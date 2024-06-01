<script setup>
import MainPanel from './components/MainPanel.vue'
import PlayerPage from './components/PlayerPage.vue'
import NavigationElement from './components/NavigationElement.vue'
import { Bar } from 'vue-chartjs'
</script>

<template>
  <NavigationElement />
  <img src="./../public/red_icon.png" alt="RWW" class="app-icon" />
  <MainPanel class="component-divider"/>
  <PlayerPage class="component-divider"/>
</template>

<style>
.app-icon {
  width: 7rem;
  position: absolute;
  z-index: 10;
  top: 0;
  left: 0;
  border-bottom-right-radius: 5px;
}

.component-divider {
  border-bottom: 16px solid #f5e8e8;
  margin-bottom: 1rem;
}
</style>