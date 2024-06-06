<template>
    <v-col cols="2" style="margin-left: 20px; text-align: left;">
      <v-list-item>{{ name }}</v-list-item>
      <v-divider></v-divider>

    <router-link v-for="{name, route} in Categories" :to="{path: route}" style="text-decoration: none; color: inherit;">  
    <v-list-item>{{name}}</v-list-item>
    </router-link>  
    </v-col>
</template>

<script setup>
import { ref } from 'vue'; 

const Categories = [
    {name: '個人資料', route: '/profile'},
    {name: '我的課程', route: '/profile/mycourses'},
    {name: '上傳課程檔案', route: '/profile/fileupload'},
    //{name: '上傳課程', route: '/profile/uploadcourse'},

]
/*const userAvatar = ref('url_to_default_avatar'); // 替換為用戶頭像的 URL
const userName = ref(''); // 初始使用者名稱設為空字串

const fetchUserInfo = () => {
  // 假設這是從後端 API 獲取的用戶信息
  const userInfo = {
    avatar: 'url_to_user_avatar',
    name: 'test' // 假設使用者名稱從後端 API 獲取為 "Amy"
  };


  // 更新用戶頭像和名稱
  userAvatar.value = userInfo.avatar;
  userName.value = userInfo.name;
};

// 在組件初始化時獲取用戶信息
fetchUserInfo();*/
</script>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      name:'',
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
          this.name = res.data.name;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
      this.getinfo();
  },
}
</script>