<template>
  <h1>登入</h1>
  <div>
    <input type="text" placeholder="請輸入姓名" />
    <input type="text" placeholder="請輸入信箱" />
    <input type="password" placeholder="請輸入密碼" />
    <button>登入</button>
    <p>
      <router-link to="/register" class="router-link-button"
        >我還沒有帳號</router-link
      >
    </p>
  </div>
</template>
<script>
export default {
  nams: "Login",
};
</script>
<style scoped>
h1 {
  margin-bottom: 30px;
  margin-top: 20px;
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
</style>