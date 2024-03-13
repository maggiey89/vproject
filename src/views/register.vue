<template>
  <!-- <img class="logo" src="./path of the logo"> -->
  
  <div class="register-container">
    <h1>註冊</h1>
    <input type="text" placeholder="請輸入姓名" />
    <input type="text" placeholder="請輸入信箱" />
    <input type="password" placeholder="請輸入密碼" />
    <input type="text" placeholder="請再次輸入密碼" />
    <!-- <input type="text" placeholder="就讀大學" /> -->
    <div>
      <label for="university">就讀大學:</label>
      <select id="university" name="university">
        <option value="">請選擇...</option>
        <option value="university1">國立台灣師範大學</option>
        <option value="university2">國立台灣大學</option>
        <option value="university3">國立台灣科技大學</option>
        <!-- 更多選項 -->
      </select>
    </div>
    <input type="text" placeholder="就讀科系" />
    <button>完成註冊</button>
    <p>
      <router-link to="/Login" class="router-link-button"
        >已經有帳號</router-link
      >
    </p>
  </div>
</template>
<script>
// import { defineComponent } from '@vue/composition-api'

export default {
  name: "Register",
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