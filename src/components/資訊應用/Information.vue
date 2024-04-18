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
          title: '半導體技術學分學程',
          content: 'null',
        },
        {
          title: '教育大數據微學分學程',
          content: 'null',
        },
        {
          title: '空間資訊學分學程',
          content: 'null',
        },
        {
          title: '大數據資料與數位評量學分學(112-2停招)',
          content: 'null',
        },
        {
          title: '資訊科技應用學分學程',
          content: 'null',
        },
        {
          title: '學習與資訊學分學(112-2申請終止)',
          content: 'null',
        },
        {
          title: '元宇宙敘事學分學程',
          content: 'null',
        },
        {
          title: '人工智慧技術與應用學分學程',
          content: 'null',
        },
        ],
      }
    },
  }
  
  </script>