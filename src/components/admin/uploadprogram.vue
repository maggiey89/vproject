<template>
  <div>
    <div class="form-group">
      <label for="programName" class="custom-label">學程名稱：</label>
      <input type="text" id="programName" v-model="newProgramName" class="custom-input" placeholder="ex:基礎管理學分學程" required>
    </div>

    <div class="form-group">
      <label for="programCategory" class="custom-label">所屬類別：</label>
      <select v-model="newProgramCategory" id="program" class="custom-select" required>
            <option  v-for="(f, index) in fields" :key="index">{{ f }}</option>
      </select>
    </div>

    <form @submit.prevent="confirmAdd">
      <div class="form-group">
        <label for="searchCourse" class="custom-label">請輸入要加入的課程代碼：</label>
        <input type="text" id="searchCourse" v-model="searchQuery" class="custom-input" placeholder="ex:PGUA005">
      </div>

      <v-list class="course-list">
        <v-list-item v-for="course in filteredCourses" :key="course.id" :value="course.id" @click="toggleCourse(course)">
          <template v-slot:prepend="{ isActive }">
            <v-list-item-action start>
              <v-checkbox-btn :model-value="isActive" color="primary"></v-checkbox-btn>
            </v-list-item-action>
          </template>
          <v-list-item-content>
            <v-list-item-title class="course-code">{{ course.code }}</v-list-item-title>
            <v-list-item-subtitle class="course-name">{{ course.name }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>


      <div class="form-group">
        <label for="programName" class="custom-label">已選課程：</label>
        <div class="selected-courses">
          <v-chip v-for="courseId in selectedCourses" :key="courseId" @click="removeCourse(courseId)">
            {{ courseId.name }}
            <v-icon small>mdi-close</v-icon>
          </v-chip>
        </div>
      </div>

      <div class="form-group">
        <button type="submit" class="submit-button">確認新增</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      courses: [],
      selectedCourses: [],
      fields: [], 
      newProgramName: '', 
      searchQuery: '', 
      showCourseList: false, 
      newProgramCategory: '',//大領域
    };
  },
  computed: {
    filteredCourses() {
      return this.courses.filter(course => {
        return course.code.toLowerCase().includes(this.searchQuery.toLowerCase());
      });
    }
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
    getcourses(){
      const path = 'http://127.0.0.1:5000/getcourses';
      axios.get(path)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    toggleCourse(courseId) {
      
      if (this.selectedCourses.includes(courseId)) {
        this.selectedCourses = this.selectedCourses.filter(id => id !== courseId);
      } else {
        this.selectedCourses.push(courseId);
      }
    },

    confirmAdd() {
      const payload = {
        field: this.newProgramCategory,
        name: this.newProgramName,
        category: this.newProgramCategory,
        courses: this.selectedCourses, 
      };
      const path = 'http://127.0.0.1:5000/addprogram';
      axios.post(path, payload)
      .then((res) => {
        if(res.data.success){
          alert("學分學程新增成功。");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },



    toggleCourseList() {
      this.showCourseList = !this.showCourseList;
    },

    getCourseName(courseId) {
      const course = this.courses.find(course => course.code === courseId);
      return course ? course.name : '';
    },

    removeCourse(courseId) {
      this.selectedCourses = this.selectedCourses.filter(id => id !== courseId);
    }
  },
  created() {
    this.getcourses();
    this.getFields();
  }
};
</script>

<!-- //----------------------------------------- -->
<style scoped>
h1 {
  margin-bottom: 2px;
  font-family: 'Arial', sans-serif;
  color: #fff; 
  background-color: rgb(190, 190, 190); 
  padding: 5px 10px; 
  border-radius: 8px; 
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
}
.form-group {
  margin-bottom: 20px;
}

.custom-label {
  display: block;
  margin-bottom: 15px;
  font-weight: bold;
  margin-top: 10px;
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

.selected-courses {
  display: flex;
  flex-wrap: wrap;
}

.selected-courses v-chip {
  margin-right: 5px;
  margin-bottom: 5px;
}

.course-list {
  max-width: 800px;
  margin: 0 auto;
  max-height: 400px; /* 固定高度 */
  overflow-y: auto; /* 垂直滚动 */
}

.course-list-item {
  padding: 10px;
  font-size: 16px;
  border-bottom: 1px solid #ddd;
}

.course-code {
  font-size: 16px;
  font-weight: bold;
}

.course-name {
  font-size: 14px;
  color: #666;
}
</style>