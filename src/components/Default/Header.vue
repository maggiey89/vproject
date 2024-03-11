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
    <div
      style="
        font-family: 'Noto Sans TC', serif;
        float: left;
        color: #ffffff;
        font-size: 20px;
        font-weight: 400;
        letter-spacing: 1px;
        padding-left: 15px;
        margin-top: 3px;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: rgba(255, 255, 255, 0.2);
        text-decoration: none;
      "
    >
      <router-link style="text-decoration: none; color: inherit" to="/">
        標題放這
      </router-link>
    </div>

    <v-spacer />

    <v-btn to="/course-view" variant="text" height="100%"> 學分學程 </v-btn>

    <v-menu open-on-hover>
      <template v-slot:activator="{ props }">
        <v-btn to="/profile" v-bind="props" variant="text" height="100%">
          個人檔案
        </v-btn>
      </template>

      <v-list density="compact">
        <router-link
          v-for="{ name, route } in profile"
          :to="{ path: route }"
          style="text-decoration: none; color: inherit"
        >
          <v-list-item>{{ name }}</v-list-item>
        </router-link>
      </v-list>
    </v-menu>

    <!--v-btn to="/profile" height="100%" class="text-body-1 font-weight-medium"
        style="background-color: #6D0116;" variant="text">
      個人檔案 
      </v-btn-->

    <v-btn to="/register" class="mr-5" variant="text" height="100%">
      註冊
    </v-btn>
    <!-- <v-btn to="/login" class="mr-5" variant="text" height="100%"> 註冊 </v-btn> -->
  </v-app-bar>
</template>
  
  <script setup>
import ntnu from "@/assets/ntnu.png";
import ntnuLogo from "@/assets/ntnu-logo.png";

const profile = [
  { name: "個人資料", route: "/profile" },
  { name: "我的課程", route: "/profile" },
  { name: "新增課程", route: "/profile/uploadcourse" },
];
</script>
<style scoped>
.v-btn {
  background-color: #6d0116;
  font-size: medium;
  font-weight: 500;
  letter-spacing: 1px;
}
</style>