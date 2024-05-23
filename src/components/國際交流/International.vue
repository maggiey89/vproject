<template>
  <v-expansion-panel v-for="data in courses" :key="data.title" :title="data.title">

    <v-progress-linear :model-value="data.complete"
      :class="{ 'redtext': data.complete < 30, 
                'yellowtext': data.complete >= 30 && data.complete < 70, 
                'greentext': data.complete >= 70 }"
    >
    </v-progress-linear>

    <v-expansion-panel-text>
      <component :is="data.content"/>
    </v-expansion-panel-text>
  </v-expansion-panel>
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
        complete: 0,
      },
      {
        title: '全英語學分學程',
        content: '全英語',
        complete: 0,
      },
      {
        title: '國際足跡學分學程',
        content: '國際足跡',
        complete: 0,
      },
      ],
    }
  },
}
  </script>

<style>
.v-data-table {
  width: 100%;
}
.v-card-title {
  text-align: center;
  margin-top: 10px;
}
</style>