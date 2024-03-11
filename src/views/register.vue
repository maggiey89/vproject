<template>
  <!-- <img class="logo" src="./path of the logo"> -->
  <h1>註冊</h1>
  <div>
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
        <option value="university3">國立台北大學</option>
        <!-- 更多選項 -->
      </select>
    </div>
    <input type="text" placeholder="就讀科系" />
    <button>完成註冊</button>
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
  margin-bottom: 40px; /* 增加底部外距 */
  margin-top: 0px;
}

input[type="text"],
input[type="password"] {
  border: 1px solid #ccc; /* 設置邊框 */
  padding-left: 20px; /* 添加內距 */
  margin-bottom: 20px; /* 設置元素間的間距 */
  margin-right: auto;
  margin-left: auto;
  background-color: rgb(255, 255, 255); /* 設置背景色 */
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
  border-radius: 8px; /* 添加圓弧角 */
  width: 320px;
  margin-bottom: 30px;
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
</style>