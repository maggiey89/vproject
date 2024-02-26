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
