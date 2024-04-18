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
          title: '社團人專業領導培力學分學程',
          content: 'null',
        },
        {
          title: '金牌書院學分學程',
          content: 'null',
        },
        {
          title: '戶外探索領導學分學程',
          content: 'null',
        },
        ],
      }
    },
  }
  
  </script>