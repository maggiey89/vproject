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

    <v-btn to="" variant="text" height="100%"> 操作手冊 </v-btn>
    <v-btn to="/course-view/business" variant="text" height="100%"> 學分學程 </v-btn>

    <!--v-btn to="/admin" variant="text" height="100%" v-if="headerfile.iden == 0 && isloggedin"> 管理者介面 </v-btn-->

    <v-menu open-on-hover v-if="headerfile.iden == 0 && isloggedin">
      <template v-slot:activator="{ props }">
        <v-btn to="/admin" v-bind="props" variant="text" height="100%">
          Admin
        </v-btn>
      </template>

      <v-list density="compact">
        <router-link v-for="{ name, route } in admin" :to="{ path: route }"
          style="text-decoration: none; color: inherit; text-align: center;">
          <v-list-item>{{ name }}</v-list-item>
        </router-link>
      </v-list>
    </v-menu>

    <v-menu open-on-hover v-if="headerfile.iden == 1 && isloggedin">
      <template v-slot:activator="{ props }">
        <v-btn to="/profile" v-bind="props" variant="text" height="100%">
          {{ headerfile.name }}
        </v-btn>
      </template>

      <v-list density="compact">
        <router-link v-for="{ name, route } in profile" :to="{ path: route }"
          style="text-decoration: none; color: inherit; text-align: center;">
          <v-list-item>{{ name }}</v-list-item>
        </router-link>
      </v-list>
    </v-menu>

    <v-btn to="/login" class="mr-5" variant="text" height="100%" v-if="!isloggedin "> 登入 </v-btn>

    <template>
      <v-dialog v-model="dialogLogout" max-width="500px">
              <v-card>
                <v-card-title class="text-h5">確定要登出嗎？</v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue-darken-1" variant="text" @click="closeLogout">取消</v-btn>
                  <v-btn to="/" color="blue-darken-1" variant="text" @click="logoutConfirm">登出</v-btn>
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>
    </template>
      <v-btn class="mr-5" variant="text" height="100%" v-if="isloggedin" @click.prevent = "logout"> 登出 </v-btn>
    
  </v-app-bar>
</template>

<script setup>
import { ref } from 'vue';


const userAvatar = ref('url_to_default_avatar'); // 替換為用戶頭像的 URL
const userName = ref(''); // 初始使用者名稱設為空字串
const userRole = ref('');

const profile = [
  { name: "個人資料", route: "/profile" },
  { name: "我的課程", route: "/profile/mycourses" },
  { name: "新增課程", route: "/profile/uploadcourse" },
];

const admin = [
  { name: "個人資料", route: "/admin" },
  { name: '所有課程', route: '/admin/showcourses'},
  { name: '新增課程', route: '/admin/uploadcourse' },
  { name: '新增學程', route: '/admin/uploadprogram' },
  { name: '新增領域', route: '/admin/uploadfield' },
  { name: '新增學程中分類', route: '/admin/subset' },
]

/*const header = () => {
  const user = JSON.parse(localStorage.getItem('user'));
  if(user && user["access_token"]){
    return {Authorization : `Bearer ${user["access_token"]}`};
  }
  else {
    return {};
  }
};

const fetchUserInfo = async() => {
  // 假設這是從後端 API 獲取的用戶信息
  if(localStorage.getItem('user')){
  const userInfo = {
    avatar: 'url_to_user_avatar',
    name: '', // 假設使用者名稱從後端 API 獲取為 "Amy"
    role: '',
  };

  const path = 'http://127.0.0.1:5000/userinfo';
  try{
    const response = await axios.get(path, { headers: header() });
    userInfo.name = response.data.name;
    userInfo.role = response.data.iden;
    userAvatar.value = userInfo.avatar;
    userName.value = userInfo.name;
    userRole = userInfo.role;
  }catch(error){
      console.error(error);
  };
  // 更新用戶頭像和名稱
  
  }
};

// 在組件初始化時獲取用戶信息
fetchUserInfo();*/
</script>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      headerfile: {
        name: '',
        iden: '',
      },
      isloggedin: false,
      dialogLogout: false,
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
    logout() {
      this.dialogLogout = true;
    },
    logoutConfirm () {
      localStorage.removeItem('user');
      if (localStorage.getItem('courseList')) {
        localStorage.removeItem('courseList')
      }
      this.closeLogout();
      //location.reload();
      router.push({name: 'home'});//不知為何不會換頁面
    },

      closeLogout () {
        this.dialogLogout = false
        
        /*this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })*/
      },
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
}
</script>


<style scoped>
/* CSS 樣式 */
</style>
