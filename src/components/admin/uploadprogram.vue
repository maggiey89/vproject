<template>
    <div>
      <h1>新增學程</h1>
      <form @submit.prevent="confirmAdd">
      <div class="form-group">
        <label for="program" class="custom-label">請選擇學程所屬領域：</label>
        <div>
          <select id="program" v-model="newprogramForm.field" class="custom-select" required>
            <option  v-for="(f, index) in fields" :key="index">{{ f }}</option>
          </select>
        </div>
      </div>
  
      <div class="form-group">
        <label for="programName" class="custom-label">請輸入新增學程名稱：</label>
        <input type="text" id="programName" v-model="newprogramForm.name" class="custom-input" placeholder="ex: 全英語學分學程" required>
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
        fields:[],
        newprogramForm:{
          name: '',
          field: '',
        }
      };
    },
    methods: {
      getFields(){
      const path = 'http://127.0.0.1:5000/getfield';
      axios.get(path)
      .then((res) => {
        this.fields = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
      },

      addprogram(payload){
        const path = 'http://127.0.0.1:5000/addprogram';
        axios.post(path, payload)
        .then(() => {
          alert('已新增完成，請到"新增課程"處新增學程內課程。');
        })
        .catch((error) => {
        console.log(error);
        })
      },

      confirmAdd() {
        const payload = {
          name: this.newprogramForm.name,
          field: this.newprogramForm.field,
        }
        this.addprogram(payload);
      }
    },
    created(){
      this.getFields();
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
  