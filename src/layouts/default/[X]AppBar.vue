<template>
  <v-app-bar flat color="#546E7A">
    <div class="ml-5">
      <a href="https://www.ntnu.edu.tw/">
        <v-img
        :src="ntnuLogo"
        @click=""
        style="float: left; width: 38px; height: 38px; margin-top: 7px;"
        />

        <v-img 
        :src="ntnu"
        style="float: left; width: 190px; padding-left: 5px; padding-right: 10px;"
        />
     </a>
    </div>
    <div style="font-family: 'Noto Serif TC', serif;
      float: left;
      color: #FFFFFF;
      font-size: 20px;
      font-weight: 400;
      letter-spacing: 1px;
      padding-left: 15px;
      margin-top: 3px;
      border-left-width: 1px;
      border-left-style: solid;
      border-left-color: rgba(255,255,255,0.2);">
      學分學程
    </div>
    <router-link to="/">

    </router-link>

    
    
      
    
    <!--v-app-bar-title>
      <v-icon icon="mdi-circle-slice-4" />

      國立臺灣師範大學
    </v-app-bar-title-->
  </v-app-bar>
</template>

<script setup>
  import ntnu from "@/assets/ntnu.png"
  import ntnuLogo from "@/assets/ntnu-logo.png"

  
</script>
