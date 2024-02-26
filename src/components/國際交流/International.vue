<template>
    <v-container style="margin-top: 50px; height: 100px; text-align: center; font-size: 30px;">
      檢視
    </v-container>
    <v-container style=" background-color: rgb(248, 248, 247); ">
      <v-row no-gutters align="start">
      <SideNav/>
  
      <v-col style="margin-left: 40px; margin-right: 20px">
        <v-expansion-panels variant="accordion" style="display: flex;">
          <v-expansion-panel v-for="{title, content} in Data">
            <v-expansion-panel-title expand-icon="mdi-menu-down">
              {{ title }}
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              <Korean/>
            </v-expansion-panel-text>
          </v-expansion-panel>
  
        </v-expansion-panels>
      </v-col>
    </v-row>
    </v-container>
  
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import SideNav from '@/components/Default/SideNav.vue'
  import Korean from '@/components/語言文學/韓國學與語文學分學程.vue'
    const Data = [
      {
        title: '國際關係與外交學分學程',
        content: 'Business',
      },
      {
        title: '全英語學分學程',
        content: 'blank',
      },
      {
        title: '全英語學分學程',
        content: 'blank',
      },
    ]
      
    //})
  </script>