<template>
  <v-expansion-panel v-for="data in courses" :key="data.complete" :title="data.title">

    <v-progress-linear v-if="isloggedin" :model-value="data.complete"
      :class="{ 'redbar': data.complete < 30, 
                'yellowbar': data.complete >= 30 && data.complete < 70, 
                'greenbar': data.complete >= 70 }"
    >
    </v-progress-linear>

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
        complete: '20',
      },
      {
        title: '財務金融學分學程',
        content: '財務金融',
        complete: '0',
      },
      {
        title: '大師創業學分學程',
        content: '大師創業',
        complete: '0',
      },
      {
        title: '國際經貿與涉外事務全英語學分學程',
        content: '國際經貿',
        complete: '0',
      },
      {
        title: '商業分析學分學程',
        content: '商業分析',
        complete: '0',
      },
      {
        title: 'ESG永續管理學分學程',
        content: 'ESG永續',
        complete: '0',
      },
      ],
      isloggedin: false,
    }
  },

  created() {
    if (localStorage.getItem('user')) {
      this.isloggedin = true;
      //this.getinfo();
    }
    else{
      this.isloggedin = false;
    }
  },

  methods: {
    header() {
      const user = JSON.parse(localStorage.getItem('user'));
      if (user && user["access_token"]) {
        return { Authorization: `Bearer ${user["access_token"]}` };
      }
      else {
        return {};
      }
    },
    /*
    getinfo() {
      const path = 'http://127.0.0.1:5000/userinfo';
      axios.get(path, { headers: this.header() })
        .then((res) => {
          this.headerfile.name = res.data.name;
          this.headerfile.iden = res.data.iden;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    */
  },
}

</script>
