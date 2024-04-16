<template>
    <div>
      <h1>新增領域</h1>
  
      <div class="form-group">
        <label for="domainName" class="custom-label">請使用者輸入領域名稱：</label>
        <input type="text" id="domainName" v-model="domainName" class="custom-input" placeholder="ex:商業管理">
      </div>
  
      <button @click="confirmAdd" class="submit-button">確認新增</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        domainName: ''
      };
    },
    methods: {
      confirmAdd() {
        alert('已新增領域，請到"新增學程"處新增學程內容。');
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
  
  .custom-input:hover {
    border-color: #aaa;
  }
  
  .custom-input:focus {
    border-color: #4d90fe;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
  }
  </style>
  