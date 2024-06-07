<template>
  <v-expansion-panel v-for="data in courses" :key="data.title" :title="data.title">

    <v-progress-linear v-if="headerfile.iden == 1 && isloggedin" :model-value="data.complete"
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
  import axios from 'axios';
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
      headerfile: {
        name: '',
        iden: '',
      },
      isloggedin: false,
    }
  },

  created() {
    if (localStorage.getItem('user')) {
      this.isloggedin = true;
      this.getinfo();
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

<style>
.v-data-table {
  width: 100%;
}
.v-card-title {
  text-align: center;
  margin-top: 10px;
}
</style>