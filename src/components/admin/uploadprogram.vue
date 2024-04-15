<template>
    <div>
      <h1>新增學程</h1>
  
      <div class="form-group">
        <label for="program" class="custom-label">請選擇學程所屬領域：</label>
        <div>
          <select id="program" v-model="selectedProgram" class="custom-select">
            <option value="商業管理">商業管理</option>
            <option value="國際交流">國際交流</option>
            <option value="專業領導">專業領導</option>
            <option value="教育發展">教育發展</option>
            <option value="文化創意">文化創意</option>
            <!-- 添加其他學程領域 -->
          </select>
        </div>
      </div>
  
      <div class="form-group">
        <label for="programName" class="custom-label">請輸入新增學程名稱：</label>
        <input type="text" id="programName" v-model="programName" class="custom-input" placeholder="ex: 全英語學分學程">
      </div>
  
      <button @click="confirmAdd" class="submit-button">確認新增</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedProgram: '',
        programName: ''
      };
    },
    methods: {
      confirmAdd() {
        // 假設這裡是提交表單的程式碼
        alert('已新增完成，請到"新增課程"處新增學程內課程。');
      }
    }
  };
  </script>
  
  <style scoped>
  h1 {
    margin-bottom: 20px;
    font-family: 'Arial', sans-serif;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 20px; 
  }
  
  .custom-label {
    display: block;
    margin-bottom: 5px; 
    font-weight: bold;
  }
  
  .custom-select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    background-color: #fff;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  }
  
  .custom-input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    background-color: #fff;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    margin-top: 5px; 
  }
  
  .submit-button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #b8bfc6;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .submit-button:hover {
    background-color: #727a83;
  }
  
  .custom-select:hover,
  .custom-input:hover {
    border-color: #aaa;
  }
  
  .custom-select:focus,
  .custom-input:focus {
    border-color: #4d90fe;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
  }
  </style>
  