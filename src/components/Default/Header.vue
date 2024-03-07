<template>
    <v-app-bar flat color="#6D0116" class="width: 100%; display: block;">
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
      <div style="font-family: 'Noto Sans TC', serif;
        float: left;
        color: #FFFFFF;
        font-size: 20px;
        font-weight: 400;
        letter-spacing: 1px;
        padding-left: 15px;
        margin-top: 3px;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: rgba(255,255,255,0.2);
        text-decoration: none;"
        >
        <router-link style="text-decoration: none; color: inherit;" to="/">
            標題放這
        </router-link>
      </div>

      <v-spacer/>

      <v-btn to="/Upload" class="mr-5 text-body-1 font-weight-medium"
        style="background-color: #6D0116;" variant="text">
      已修課程 
      </v-btn>

      <v-btn to="/Login" class="mr-5 text-body-1 font-weight-medium"
        style="background-color: #6D0116;" variant="text">
      登入 
      </v-btn>
      
    </v-app-bar>
  </template>
  
  <script setup>
    import ntnu from "@/assets/ntnu.png"
    import ntnuLogo from "@/assets/ntnu-logo.png"
  
    
  </script>
  