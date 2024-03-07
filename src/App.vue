<template>
  <v-app>
    <v-container>
      <default-bar/>
    </v-container>
    <v-container/>
    <router-view />
  </v-app>
</template>

<script setup>
import DefaultBar from '@/components/Default/Header.vue'
</script>

<style>
/* Import the font */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');

/* Apply the font globally */
html, body, .v-application {
  font-family: 'Noto Sans SC', sans-serif;
}
</style>