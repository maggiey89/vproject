<template>
  <!-- <img class="logo" src="./path of the logo"> -->

  <div class="register-container">
    <h1>註冊</h1>
    <!--<h3 v-if="showmessage" show>{{ message }}</h3>-->
    <form @submit="onSubmit">
      <input type="text" v-model="newuserform.name" placeholder="請輸入姓名" />
      <input type="text" v-model="newuserform.email" placeholder="請輸入信箱" />
      <input type="password" v-model="newuserform.password1" placeholder="請輸入密碼" />
      <input type="password" v-model="newuserform.password2" placeholder="請再次輸入密碼" />
      <!-- <input type="text" placeholder="就讀大學" /> -->
      <div>
        <label for="university">就讀大學:</label>
        <select id="university" name="university" v-model="newuserform.school">
          <option value="">請選擇...</option>
          <option  v-for="(s, index) in schools" :key="index">{{ `${s.abbr} ${s.name}` }}</option>
          <!--<option value="university2">國立台灣大學</option>
          <option value="university3">國立台灣科技大學</option>-->
          <!-- 更多選項 -->
        </select>
      </div>
      <input type="text" v-model="newuserform.department" placeholder="就讀科系" />
      <button type="submit">完成註冊</button>
    </form>
    <p>
      <router-link to="/Login" class="router-link-button"
        >已經有帳號</router-link
      >
    </p>
  </div>
</template>
<script>
// import { defineComponent } from '@vue/composition-api'
import axios from 'axios';

export default {
  name: "Register",
  data() {
    return {
      schools: [],
      newuserform : {
      name: '',
      email: '',
      password1: '',
      password2: '',
      school: '',
      department: '',
}
    }
  },
  methods : {
    getSchools(){
      const path = 'http://127.0.0.1:5000/school';
      axios.get(path)
      .then((res) => {
        this.schools = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
    },

    signup(payload){
      const path = 'http://127.0.0.1:5000/signup';
      axios.post(path, payload)
      .then(() => {
        this.message = '註冊成功！請登入';
        this.showmessage = true;
      })
      .catch((error) => {
        console.log(error);
      })
    },

    onSubmit(){
      if(this.newuserform.password1 == this.newuserform.password2)
      {
        const payload = {
          name: this.newuserform.name,
          email: this.newuserform.email,
          password: this.newuserform.password1,
          school: this.newuserform.school,
          department: this.newuserform.department,
        }
        this.signup(payload);
      }
      else
      {
        this.message = '密碼不相同！';
        this.showmessage = true;
      }
    }
  },
  created(){
    this.getSchools();
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
  margin-bottom: 20px;
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
.register-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>