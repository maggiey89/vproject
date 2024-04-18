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
  import 榮譽英語 from './榮譽英語.vue'
  import 歐洲文化與語言 from './歐洲文化與語言.vue'
  import 日本語文 from './日本語文.vue'
  import 韓國學 from './韓國學與語文.vue'
  import 文學創作 from './文學創作.vue'
  import 中英翻譯 from './中英翻譯.vue'
  
  export default {
  components: {
    SideNav, 榮譽英語, 歐洲文化與語言, 日本語文, 韓國學, 文學創作, 中英翻譯
  },
  data() {
    return {
      courses: [
      {
        title: '榮譽英語學分學程',
        content: '榮譽英語',
      },
      {
        title: '歐洲文化與語言學分學程',
        content: '歐洲文化與語言',
      },
      {
        title: '日本語文學分學程',
        content: '日本語文',
      },
      {
        title: '韓國學與語文學分學程',
        content: '韓國學',
      },
      {
        title: '文學創作學分學程',
        content: '文學創作',
      },
      {
        title: '中英翻譯學分學程',
        content: '中英翻譯',
      },
      ],
    }
  },
}
  </script>