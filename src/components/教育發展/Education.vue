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
        title: '音樂輔導與特教學分學程',
        content: 'null',
      },
      {
        title: '肌力與體能訓練學分學程',
        content: 'null',
      },
      {
        title: '原住民族教育文化學分學程',
        content: 'null',
      },
      {
        title: '學校心理學學分學程(112-2停招)',
        content: 'null',
      },
      {
        title: '哲學學分學程',
        content: 'null',
      },
      {
        title: '國際教師學分學程',
        content: 'null',
      },
      {
        title: '社區高齡者服務人才培力學分學程',
        content: 'null',
      },
      {
        title: 'PASSION偏鄉優質教育學分學程',
        content: 'null',
      },
      {
        title: '產業實習學分學程',
        content: 'null',
      },
      ],
    }
  },
}

</script>