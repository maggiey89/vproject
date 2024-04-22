<template>
  <v-app-bar flat color="#6D0116" class="width: 100%; display: block;">
    <div class="ml-5">
      <a href="https://www.ntnu.edu.tw/">
        <!--v-img
          :src="ntnuLogo"
          @click=""
          style="float: left; width: 38px; height: 38px; margin-top: 7px;"
          />
  
          <v-img 
          :src="ntnu"
          style="float: left; width: 190px; padding-left: 5px; padding-right: 10px;"
          /-->
      </a>
    </div>
    <div style="
        font-family: 'Noto Sans TC', serif;
        float: left;
        color: #ffffff;
        font-size: 30px;
        font-weight: bold;
        letter-spacing: 5px;
        padding-left: 15px;
        margin-top: 3px;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: rgba(255, 255, 255, 0.2);
        text-decoration: none;
      ">
      <router-link style="text-decoration: none; color: inherit" to="/">
        學分學程管理系統
      </router-link>
    </div>

    <v-spacer />

    <v-btn to="/admin" variant="text" height="100%"> 管理者介面 </v-btn>

    <v-btn to="" variant="text" height="100%"> 操作手冊 </v-btn>
    <v-btn to="/course-view/business" variant="text" height="100%"> 學分學程 </v-btn>

    <v-menu open-on-hover>
      <template v-slot:activator="{ props }">
        <v-btn to="/profile" v-bind="props" variant="text" height="100%">
          {{ userName }}
        </v-btn>
      </template>

      <v-list density="compact">
        <router-link v-for="{ name, route } in profile" :to="{ path: route }"
          style="text-decoration: none; color: inherit; text-align: center;">
          <v-list-item>{{ name }}</v-list-item>
        </router-link>
      </v-list>
    </v-menu>

    <v-btn to="/" class="mr-5" variant="text" height="100%"> 登出 </v-btn>
    <!-- // -->

    <!--v-btn to="/profile" variant="text" height="100%">
      {{ userName }}
    </v-btn-->

    <!-- <v-avatar class="mr-3" size="36">
      <img :src="userAvatar" alt="User Avatar">
    </v-avatar> -->


  </v-app-bar>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const userAvatar = ref('url_to_default_avatar'); // 替換為用戶頭像的 URL
const userName = ref(''); // 初始使用者名稱設為空字串
const userRole = ref('');

const profile = [
  { name: "個人資料", route: "/profile" },
  { name: "我的課程", route: "/profile/mycourses" },
  { name: "新增課程", route: "/profile/uploadcourse" },
];

const header = () => {
  const user = JSON.parse(localStorage.getItem('user'));
  if(user && user["access_token"]){
    return {Authorization : `Bearer ${user["access_token"]}`};
  }
  else {
    return {};
  }
};

const fetchUserInfo = () => {
  // 假設這是從後端 API 獲取的用戶信息
  const userInfo = {
    avatar: 'url_to_user_avatar',
    name: '', // 假設使用者名稱從後端 API 獲取為 "Amy"
    role: '',
  };
  const path = 'http://127.0.0.1:5000/userinfo';
  axios.get(path, { headers : header() })
  .then((res) => {
    userName.value = res.data.name;
    userInfo.role = res.data.iden;
  })
  .catch((error) => {
    console.error(error);
  });
  // 更新用戶頭像和名稱
  userAvatar.value = userInfo.avatar;
  userName.value = userInfo.name;
  userRole.value = userInfo.role;
};

// 在組件初始化時獲取用戶信息
fetchUserInfo();



</script>


<style scoped>
/* CSS 樣式 */
</style>
