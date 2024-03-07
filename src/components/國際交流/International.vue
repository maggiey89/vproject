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
  import 國際關係 from './國際關係.vue'
  import 全英語 from './全英語.vue'
  import 國際足跡 from './國際足跡.vue'
  export default {
  components: {
    SideNav, 國際關係, 全英語, 國際足跡,
  },
  data() {
    return {
      courses: [
      {
        title: '國際關係與外交學分學程',
        content: '國際關係',
      },
      {
        title: '全英語學分學程',
        content: '全英語',
      },
      {
        title: '國際足跡學分學程',
        content: '國際足跡',
      },
      ],
    }
  },
}
  </script>