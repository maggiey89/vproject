<template>
  <div class="profile-container">
    <p class="profile-item"><strong>姓名：</strong>{{ this.profile.name }}</p>
    <p class="profile-item"><strong>信箱：</strong>{{ this.profile.email }}</p>
    <p class="profile-item"><strong>大學：</strong>{{ this.profile.university }}</p>
    <p class="profile-item"><strong>就讀科系：</strong>{{ this.profile.major }}</p>
    <p class="profile-item"><strong>身分：</strong>{{ this.profile.iden }}</p>
  </div>
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
    getinfo(){
      const path = 'http://127.0.0.1:5000/userinfo';
      axios.get(path)
      .then((res) => {
        this.profile.email = res.data.email;
        this.profile.name = res.data.name;
        this.profile.university = res.data.university;
        this.profile.major = res.data.major;
        this.profile.iden = res.data.iden;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  },
  created(){
    this.getinfo();
  }
}

</script>