<template>
  <div class="profile-container">
    <p class="profile-item"><strong>姓名：</strong>{{ this.profile.name }}</p>
    <p class="profile-item"><strong>信箱：</strong>{{ this.profile.email }}</p>
    <p class="profile-item"><strong>大學：</strong>{{ this.profile.university }}</p>
    <p class="profile-item"><strong>就讀科系：</strong>{{ this.profile.major }}</p>
    <p class="profile-item"><strong>身分：</strong>{{ this.profile.iden }}</p>
  </div>
  <form @submit = "logout">
    <v-btn type="submit">登出</v-btn>
  </form>
</template>

<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 20px;
}

.profile-item {
  font-size: 16px;
  margin: 0;
  gap: 30px;
}
</style>

<script>
import ProfileNav from "@/components/Default/ProfileNav.vue";
import router from "@/router";
import axios from "axios";
// 從後端獲得使用者的個人資料
export default {
  data() {
    return {
      profile : {
      name: '',
      email: '',
      university: '',
      major: '',
      iden: '',
      }
    }
  },

  methods: {
  header(){
      const user = JSON.parse(localStorage.getItem('user'));
      if(user && user["access_token"]){
        return {Authorization : `Bearer ${user["access_token"]}`};
      }
      else {
        return {};
      }
    },
    getinfo(){
      const path = 'http://127.0.0.1:5000/userinfo';
      axios.get(path, { headers : this.header() })
      .then((res) => {
        this.profile.email = res.data.email;
        this.profile.name = res.data.name;
        this.profile.university = res.data.university;
        this.profile.major = res.data.major;
        if(res.data.iden == 1)
          this.profile.iden = '學生';
        else if(res.data.iden == 0)
          this.profile.iden = '管理者';
      })
      .catch((error) => {
        console.error(error);
      });
    },
    logout(){
      localStorage.removeItem('user');
      localStorage.removeItem('courseList')
      //router.push('/');不知為何不會換頁面
    }
  },
  created(){
    if(localStorage.getItem('user')){
      this.getinfo();
    }
  }
}

</script>