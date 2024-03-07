<template>
    <v-container style="margin-top: 50px; height: 100px; text-align: center; font-size: 30px;">
      檢視
    </v-container>
    <v-container style=" background-color: rgb(248, 248, 247); margin-bottom: 50px; height: 100%;">
      <v-row no-gutters align="start">
      <SideNav/>
  
      <v-col style="margin-left: 40px; margin-right: 20px">
        <v-expansion-panels variant="accordion" style="display: flex;">

          <v-expansion-panel v-for="data in courses" :key="data.title" :title="data.title">
          <!--v-expansion-panel-title expand-icon="mdi-menu-down">
            {{ data.title }}
          </v-expansion-panel-title-->
          <v-expansion-panel-text>
            <component :is="data.content"/>
          </v-expansion-panel-text>
        </v-expansion-panel>

        </v-expansion-panels>
      </v-col>
    </v-row>
    </v-container>
  
  </template>
  
  <script>
  import { ref } from 'vue'
  import SideNav from '@/components/Default/SideNav.vue'
  import 韓國學 from '@/components/語言文學/韓國學與語文.vue'
  export default {
  components: {
    SideNav, 韓國學,
  },
  data() {
    return {
      courses: [
      {
        title: '榮譽英語學分學程',
        content: 'Business',
      },
      {
        title: '歐洲文化與語言學分學程',
        content: 'blank',
      },
      {
        title: '日本語文學分學程',
        content: 'blank',
      },
      {
        title: '韓國學與語文學分學程',
        content: '韓國學',
      },
      {
        title: '文學創作學分學程',
        content: 'blank',
      },
      {
        title: '中英翻譯學分學程',
        content: 'blank',
      },
      ],
    }
  },
}
  </script>