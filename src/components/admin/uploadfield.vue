<template>
    <div>
      <h1>新增領域</h1>
      <!--v-form @submit="confirmAdd" >
        <label for="domainName" class="custom-label">請使用者輸入領域名稱：</label>
        <v-text-field type="text" id="domainName" v-model="domainName" label="ex: 商業管理" placeholder=" "
        variant="solo" density="compact"/>
      </v-form-->

      <form @submit="confirmAdd">
        <div class="form-group">
          <label for="domainName" class="custom-label">請使用者輸入領域名稱：</label>
          <input type="text" id="domainName" v-model="domainName" class="custom-input" placeholder="ex:商業管理">
        </div>
  
        <button type="submit" class="submit-button">確認新增</button>
      </form>
    </div>
</template>
  
<script>
import axios from 'axios';
  export default {
    data() {
      return {
        domainName: ''
      };
    },
    methods: {
      addfield(payload){
        const path = 'http://127.0.0.1:5000/addfield';
        axios.post(path, payload)
        .then(() => {
          alert('已新增領域，請到"新增學程"處新增學程內容。');
        })
        .catch((error) => {
        console.log(error);
        })
      },

      confirmAdd() {
        const payload = {
          name: this.domainName,
        }
        this.addfield(payload);
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
  