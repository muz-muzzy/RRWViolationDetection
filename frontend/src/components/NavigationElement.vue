<template>
    <nav class="navigation-bar">
      <VaIcon name="menu" />
      <ul>
        <li v-for="(item, index) in items" :key="index" @click="scrollToSection(index)">
          {{ item }}
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        items: ['Начальная', 'Просмотр', 'Статистика'],
      };
    },
    methods: {
      scrollToSection(sectionIndex) {
        const sectionHeight = window.innerHeight;
        const targetPosition = sectionIndex * sectionHeight;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
      },
    },
  };
  </script>
  
  <style scoped>
  .navigation-bar {
    position: fixed;
    border-bottom-left-radius: 8px;
    right: 0;
    top: 0; 
    font-size: 0.8em;
    background-color: #e63c3c;
    font-weight: bold;
    color: white;
    padding-left: 0.5rem;
    padding-right: 1rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    transition: 250ms ease; 
  }
  
  .navigation-bar ul {
    list-style-type: none;
    padding: 0;
  }
  
  .navigation-bar li {
    cursor: pointer;
    border-radius: 5px;
    margin: 0.35rem;
    padding: 0.35rem;
    transition: 250ms ease; 
  }
  
  .navigation-bar:hover {
    transition: 350ms ease; 
  }

  .navigation-bar li:hover {
    background-color: #e63c3c;
    font-size: 1.5em;
    padding: 0.5rem; 
    transition: 350ms ease; 
  }
  </style>