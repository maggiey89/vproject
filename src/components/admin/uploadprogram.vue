<template>
  <div>
    <h1>新增學程</h1>
    <form @submit.prevent="confirmAdd">
      <div class="form-group">
        <label class="custom-label">請選擇要加入的課程：</label>
        <div class="course-grid">
          <label v-for="(course, index) in courses" :key="index" class="course-checkbox">
            <input type="checkbox" v-model="selectedCourses" :value="course.id"> {{ course.name }}
          </label>
        </div>
      </div>

      <div class="form-group">
        <label for="programName" class="custom-label">請輸入新增學程名稱：</label>
        <input type="text" id="programName" v-model="newProgramName" class="custom-input" placeholder="ex: 全英語學分學程" required>
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
      courses: [{"id": 1, "name": "程式設計入門"},
    {"id": 2, "name": "網頁開發基礎"},
    {"id": 3, "name": "資料結構與演算法"},
    {"id": 4, "name": "人工智慧導論"},
    {"id": 5, "name": "數據分析實戰"},], // 存放從後端取得的課程列表
      selectedCourses: [], // 存放使用者選擇的課程
      newProgramName: '', // 新增學程的名稱
    };
  },
  methods: {
    // 從後端取得課程列表
    getCourses() {
      const path = 'http://127.0.0.1:5000/getcourses';
      axios.get(path)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    // 新增學程
    addProgram(payload) {
      const path = 'http://127.0.0.1:5000/addprogram';
      axios.post(path, payload)
        .then(() => {
          alert('已新增完成，請到"新增課程"處新增學程內課程。');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 確認新增
    confirmAdd() {
      const payload = {
        name: this.newProgramName,
        courses: this.selectedCourses, // 將使用者選擇的課程一併傳送到後端
      };
      this.addProgram(payload);
    }
  },
  created() {
    this.getCourses();
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
    margin-bottom: 15px; 
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
  .course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}

.course-checkbox {
  display: block;
}

  </style>
  