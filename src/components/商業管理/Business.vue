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
import 基礎管理 from './基礎管理.vue'
import 財務金融 from './財務金融.vue'
import 大師創業 from './大師創業.vue'
import 國際經貿 from './國際經貿.vue'
import 商業分析 from './商業分析.vue'
import ESG永續 from './ESG永續.vue'
export default {
  components: {
    SideNav, 基礎管理, 財務金融, 大師創業, 國際經貿, 商業分析, ESG永續,
  },
  data() {
    return {
      courses: [
      {
        title: '基礎管理學分學程',
        content: '基礎管理',
      },
      {
        title: '財務金融學分學程',
        content: '財務金融',
      },
      {
        title: '大師創業學分學程',
        content: '大師創業',
      },
      {
        title: '國際經貿與涉外事務全英語學分學程',
        content: '國際經貿',
      },
      {
        title: '商業分析學分學程',
        content: '商業分析',
      },
      {
        title: 'ESG永續管理學分學程',
        content: 'ESG永續',
      },
      ],
    }
  },
}

</script>