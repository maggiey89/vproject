<template>
    <v-expansion-panel v-for="data in courses" :key="data.title" :title="data.title">
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
          complete: '0',
        },
        {
          title: '金牌書院學分學程',
          content: 'null',
          complete: '0',
        },
        {
          title: '戶外探索領導學分學程',
          content: 'null',
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