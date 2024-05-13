<template>
  <div>
    <h1>新增領域</h1>
    <form @submit.prevent="confirmAdd">
      <div class="form-group">
        <label for="domainName" class="custom-label">請使用者輸入領域名稱：</label>
        <input type="text" id="domainName" v-model="domainName" class="custom-input" placeholder="ex:商業管理">
      </div>

      <div class="form-group">
        <label class="custom-label">請選擇要加入的學程：</label>
        <div class="course-grid">
          <label v-for="(program, index) in programs" :key="index" class="program-checkbox">
            <input type="checkbox" v-model="selectedPrograms" :value="program.id"> {{ program.name }}
          </label>
        </div>
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
      domainName: '',
      programs: [{"id": 1, "name": "全英語學分學程"},
      {"id": 2, "name": "程式設計學分學程"},
      {"id": 3, "name": "商業管理學分學程"},
      {"id": 4, "name": "數據分析學分學程"},
      {"id": 5, "name": "創意寫作學分學程"},
      {"id": 6, "name": "人工智慧應用學分學程"},
      {"id": 7, "name": "全球化研究學分學程"},], // 從後端取得的學程列表
      selectedPrograms: [] // 存放使用者選擇的學程
    };
  },
  methods: {
    addField(payload) {
      const path = 'http://127.0.0.1:5000/addfield';
      axios.post(path, payload)
        .then(() => {
          alert('已新增領域，請到"新增學程"處新增學程內容。');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    confirmAdd() {
      const payload = {
        name: this.domainName,
        programs: this.selectedPrograms // 將使用者選擇的學程一併傳送到後端
      };
      this.addField(payload);
    },

    // 從後端取得學程列表
    getPrograms() {
      const path = 'http://127.0.0.1:5000/getprograms';
      axios.get(path)
        .then((res) => {
          this.programs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getPrograms();
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

.course-grid {
  display: flex;
  flex-wrap: wrap;
}

.program-checkbox {
  width: calc(33.33% - 10px); 
  margin-right: 10px; 
  margin-bottom: 10px; 
  margin-top: 5px;
  text-align: left;
}




</style>
