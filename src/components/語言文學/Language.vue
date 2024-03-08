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