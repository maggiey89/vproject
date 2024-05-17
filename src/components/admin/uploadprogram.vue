<template>
  <div>
    <h1>新增學程</h1>
    <div class="form-group">
      <label for="programName" class="custom-label">學程名稱：</label>
      <input type="text" id="programName" v-model="newProgramName" class="custom-input" placeholder="請輸入學程名稱">
    </div>

    <form @submit.prevent="confirmAdd">
      <div class="form-group">
        <label for="searchCourse" class="custom-label">請輸入要加入的課程代碼：</label>
        <input type="text" id="searchCourse" v-model="searchQuery" class="custom-input" placeholder="請輸入課程代碼">
        <button type="button" class="toggle-button" @click="toggleCourseList">
          {{ showCourseList ? '隱藏清單' : '顯示清單' }}
        </button>
      </div>

      <v-list v-show="showCourseList">
        <v-list-item v-for="course in filteredCourses" :key="course.code">
          <template v-slot:default="{ active }">
            <v-list-item-action>
              <v-checkbox-btn :model-value="active" color="primary" @click="toggleCourse(course.code)"></v-checkbox-btn>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ course.code }}</v-list-item-title>
              <v-list-item-subtitle>{{ course.name }}</v-list-item-subtitle>
            </v-list-item-content>
          </template>
        </v-list-item>
      </v-list>

      <div class="form-group">
        <label for="programName" class="custom-label">已選課程：</label>
        <div class="selected-courses">
          <v-chip v-for="courseId in selectedCourses" :key="courseId" @click="removeCourse(courseId)">
            {{ getCourseName(courseId) }}
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
      newProgramName: '', 
      searchQuery: '', 
      showCourseList: false, 
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
        name: this.newProgramName,
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
  }
};
</script>

<!-- //----------------------------------------- -->
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
.course-grid {
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-gap: 10px;
}

.course-checkbox {
display: block;
}
.toggle-button {
  margin-top: 10px;
  background-color: #b8bfc6;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  padding: 8px 16px;
  margin-left: 10px; 
}

.toggle-button:hover {
  background-color: #727a83;
}

.selected-courses {
  display: flex;
  flex-wrap: wrap;
}

.selected-courses v-chip {
  margin-right: 5px;
  margin-bottom: 5px;
}
</style>
  