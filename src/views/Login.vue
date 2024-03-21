<template>
  <div class="login-container">
    <h1>登入</h1>
    <!-- <input type="text" placeholder="請輸入姓名" /> -->
    <form @submit="onSubmit">
      <input type="text" v-model="userForm.email" placeholder="請輸入信箱" />
      <input type="password" v-model="userForm.password" placeholder="請輸入密碼" />
      <button type="submit">登入</button>
    </form>
    <p>
      <router-link to="/register" class="router-link-button"
        >我還沒有帳號</router-link
      >
    </p>
  </div>
  <!--<p v-if="showmessage" >{{ message }}</p>-->
</template>
<script>
export default {
  nams: "Login",
  data() {
    return {
      userForm : {
        email: '',
        password: '',
      }
    }
  },

  methods: {
    login(){
      const path = 'http://127.0.0.1:5000/login';
      axios.post(path, payload)
      .then(() => {
        this.message = '登入成功';
        this.showmessage = true;
      })
      .catch((error) => {
        console.log(error);
      })
    },

    onSubmit(){
      const payload = {
        email: this.userForm.email,
        password: this.userForm.password,
      }
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