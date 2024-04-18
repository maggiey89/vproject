<template>
    <v-expansion-panel v-for="data in courses" :key="data.title" :title="data.title">
            <!--v-expansion-panel-title expand-icon="mdi-menu-down">
              {{ data.title }}
            </v-expansion-panel-title-->
      <v-expansion-panel-text>
        <component :is="data.content"/>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </template>
  
  <script>
  import SideNav from '@/components/Default/SideNav.vue'

  export default {
    components: {
      SideNav,
    },
    data() {
      return {
        courses: [
        {
          title: '理工創新與實作學分學程',
          content: 'null',
        },
        {
          title: '天文與重力學分學程',
          content: 'null',
        },
        {
          title: '數位科技藝術學分學程',
          content: 'null',
        },
        {
          title: '電腦音樂與音訊技術學分學程學程',
          content: 'null',
        },
        {
          title: '科學計算與跨域應用EMI學分學程',
          content: 'null',
        },
        {
          title: '科技化教學產業學分學程',
          content: 'null',
        },
        {
          title: '環境監測與防災學分學程',
          content: 'null',
        },
        {
          title: '運動傷害防護學分學程',
          content: 'null',
        },
        {
          title: '區域與觀光規劃學分學程',
          content: 'null',
        },
        {
          title: '科學計算學分學程',
          content: 'null',
        },
        {
          title: '太陽能源與工程學分學程',
          content: 'null',
        },
        {
          title: '國立臺灣師範大學與台灣積體電路製造公司半導體學分學程',
          content: 'null',
        },
        ],
      }
    },
  }
  
  </script>