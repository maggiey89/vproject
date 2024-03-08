<template>
    <v-container style="margin-top: 50px; height: 100px; text-align: center; font-size: 30px;">
      檢視
    </v-container>
    <v-container style=" background-color: rgb(248, 248, 247); margin-bottom: 50px; height: 100%; ">
      <v-row no-gutters align="start">
      <SideNav/>
      <v-col style="margin-left: 40px; margin-right: 20px">

        <v-expansion-panels variant="accordion" style="display: flex; font-family: 'Noto Sans TC', serif;">
          <router-view/>
        </v-expansion-panels>
        
      </v-col>
    </v-row>
    </v-container>
  
  </template>
  
  <script setup>
  import SideNav from '@/components/Default/SideNav.vue'

  </script>