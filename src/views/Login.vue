<template>
  <div class="login-container">
    <h1>登入</h1>
    <!-- <input type="text" placeholder="請輸入姓名" /> -->
    <form @submit.prevent="onSubmit">
      <!--input type="text" v-model="userForm.email" 
        placeholder="請輸入信箱" />
      <input type="password" v-model="userForm.password" 
        placeholder="請輸入密碼" /-->
      <v-text-field type="email" v-model="userForm.email"
        label="請輸入信箱" placeholder="johndoe@gmail.com" 
        variant="outlined" density="compact"/>
      <v-text-field type="password" v-model="userForm.password" 
        label="請輸入密碼" placeholder="********"
        variant="outlined" density="compact"/>

      <button type="submit">登入</button>
    </form>
    <p>
      <router-link to="/register" class="router-link-button"
        >我還沒有帳號</router-link
      >
    </p>
  </div>
  <!--<p v-if="showmesssge" >{{ message }}</p>-->
</template>
<script>
import router from '@/router';
import axios from 'axios';
export default {
  nams: "Login",
  data() {
    return {
      message: '',
      showmessage: false,
      userForm : {
        email: '',
        password: '',
      }
    }
  },

  methods: {
    login(payload){
      const path = 'http://127.0.0.1:5000/login';
      axios.post(path, payload)
      .then((res) => {
        if(res.data.access_token){
          localStorage.setItem('user', JSON.stringify(res.data));//登出按鈕
          router.push('/');
        }
      })
      .catch((error) => {
        console.log(error);
        this.message = "not success.";//有能顯示錯誤訊息的地方嗎？
        this.showmessage = true;
      })
    },

    onSubmit(){
      const payload = {
        email: this.userForm.email,
        password: this.userForm.password,
      }
      this.login(payload);
    }
  }
};
</script>
<style scoped>
h1 {
  margin-bottom: 20px;
  margin-top: 50px;
}

input[type="text"],
input[type="password"] {
  border: 1px solid #ccc;
  padding-left: 20px;
  margin-bottom: 20px;
  margin-right: auto;
  margin-left: auto;
  background-color: rgb(255, 255, 255);
  width: 320px;
  height: 40px;
  display: block;
}

button {
  border: none;
  padding: 10px 20px;
  background-color: #84a8cf;
  color: white;
  cursor: pointer;
  border-radius: 8px;
  width: 320px;
  margin-bottom: 20px;
  margin-top: 10px;
}

button:hover {
  background-color: #637485;
}
select {
  width: 320px;
  height: 50px;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 30px;
  background-color: white;
  display: block;
  margin-right: auto;
  margin-left: auto;
  margin-top: 10px;
}
.router-link-button {
  display: block;
  width: 320px;
  padding: 10px 20px;
  margin: 10px auto 30px;
  text-align: center;
  background-color: #84a8cf;
  color: white;
  border-radius: 8px;
  text-decoration: none;
  cursor: pointer;
  margin-top: 10px;
}

.router-link-button:hover {
  background-color: #637485;
}
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>