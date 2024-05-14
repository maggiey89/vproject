<template>
  <div>
    <h1>新增課程</h1>

    <!-- <div class="form-group">
      <label for="program" class="custom-label">請選擇課程所屬學程領域：</label>
      <div>
        <select id="program" v-model="newcourseForm.field" class="custom-select" required>
          <option  v-for="(f, index) in fields" :key="index">{{ f }}</option>
        </select>
      </div>
    </div>

    <div class="form-group">
      <label for="courseName" class="custom-label">請輸入新增課程所屬學程：</label>
      <select id="program" v-model="newcourseForm.program" class="custom-select" required>
          <option  v-for="(p, index) in programs" :key="index">{{ p }}</option>
        </select>
    </div>

    <div class="form-group">
      <label for="programType" class="custom-label">請選擇課程類型：</label>
      <div>
        <select id="programType" v-model="newcourseForm.type" class="custom-select" required>
          <option value="必修">必修</option>
          <option value="選修">選修</option>
        </select>
      </div>
    </div> -->

    <div class="form-group">
      <label for="courseName" class="custom-label">請輸入課程名稱：</label>
      <input type="text" id="courseName" v-model="newcourseForm.name" class="custom-input" placeholder="ex: 初級韓文" required>
    </div>

    <div class="form-group">
      <label for="courseCode" class="custom-label">請輸入課程代碼：</label>
      <input type="text" id="courseCode" v-model="newcourseForm.code" maxlength="7" class="custom-input" placeholder="ex: L0U2001" required>
    </div>

    <div class="form-group">
      <label for="credit" class="custom-label">請輸入學分數：</label>
      <input type="text" id="credit" v-model="newcourseForm.credit" class="custom-input" placeholder="輸入數字" required>
    </div>

    <button @click="submitForm" class="submit-button">確認送出</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      newcourseForm:{
        name: '',
        code: '',
        credit: '',
        
      },         
    };
  },
  methods: {
    submitForm() {
      const payload = {
        name: this.newcourseForm.name,
        code: this.newcourseForm.code,
        credit: this.newcourseForm.credit,
      }
      const path = 'http://127.0.0.1:5000/addcourse';
      axios.post(path, payload)
      .then(() => {
        console.log('表單已提交');
        alert('已新增課程。');
      })
      .catch((error) => {
        console.error(error);
      });
      
    }
  },
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
