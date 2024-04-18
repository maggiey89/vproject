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
          title: '室內設計學分學程',
          content: 'null',
        },
        {
          title: '數位人文與藝術學分學程(112-2申請終止)',
          content: 'null',
        },
        {
          title: '知識轉譯與文化創生學分學程',
          content: 'null',
        },
        {
          title: '文物保存修復學分學程',
          content: 'null',
        },
        ],
      }
    },
  }
  
  </script>