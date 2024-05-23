<template>
    <div>
      <h1>新增小領域</h1>
      <form @submit="submitForm">
        <div class="form-group">
          <label for="field" class="custom-label">領域:</label>
          <select v-model="newsubsetForm.field" id="field" class="custom-select" required>
            <option  v-for="(f, index) in fields" :key="index">{{ f }}</option>
          </select>
        </div>
  
        <div class="form-group">
          <label for="program" class="custom-label">學程:</label>
          <select v-model="newsubsetForm.program" id="program" class="custom-select" required>
            <option  v-for="(p, index) in programs" :key="index">{{ p }}</option>
          </select>
        </div>

        <div class="form-group">
          <label for="subfield" class="custom-label">小領域課程名稱:</label>
          <input type="text" id="subfield" v-model="newsubsetForm.name" class="custom-input" placeholder="ex:資訊工程基礎領域" required>
        </div>


        <h2>課程列表:</h2>
        <v-list class="course-list">
          <v-list-item v-for="course in courses" :key="course.id" :value="course.id" @click="toggleCourse(course.code)">
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
  
        <!-- <div class="form-group">
          <label class="custom-label">必選或選修:</label>
          <input type="radio" id="compulsory" value="compulsory" v-model="newsubsetForm.type">
          <label for="compulsory">必修</label>
          <input type="radio" id="elective" value="elective" v-model="newsubsetForm.type">
          <label for="elective">選修</label>
        </div> -->
  
        <div class="form-group">
          <label for="credits" class="custom-label">最低學分:</label>
          <input type="number" id="credits" v-model="newsubsetForm.credit" class="custom-input" placeholder="輸入數字">
        </div>
        <!--div v-if="selectionType === 'compulsory'" class="form-group">
          <label for="credits" class="custom-label">最低學分:</label>
          <input type="number" id="credits" v-model="newsubsetForm.credit" class="custom-input" placeholder="輸入數字">
        </div-->
  
        <button type="submit" class="submit-button">確定</button>
      </form>
    </div>
</template>
  
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        fields: [],
        programs: [],
        courses: [],
        newsubsetForm:{
          field: '',
          program: '',
          name: '',
          course: [],
          credit: 0,
        },
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

      getProgram(f){
        const path = 'http://127.0.0.1:5000/getprogram';
        axios.post(path, f)
        .then((res) => {
          this.programs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getcourses(p){
        const path = 'http://127.0.0.1:5000/getcourses';
        const program = p;
        axios.post(path, program)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      toggleCourse(courseId) {
        if (this.newsubsetForm.course.includes(courseId)) {
          this.newsubsetForm.course = this.newsubsetForm.course.filter(id => id !== courseId);
        } else {
          this.newsubsetForm.course.push(courseId);
        }
      },

      submitForm() {
        const payload = {
          field: this.newsubsetForm.field,
          program: this.newsubsetForm.program,
          name: this.newsubsetForm.name,
          course: this.newsubsetForm.course,
          credit: this.newsubsetForm.credit,
        }
        const path = 'http://127.0.0.1:5000/addsubset';
        axios.post(path, payload)
        .then((res) => {
          if(res.data.success){
            console.log('表單已提交');
          alert('領域新增成功。');
          }
        })
        .catch((error) => {
          console.error(error);
        });
      }
    },

    created(){
    this.getFields();
    },

    watch: {
      "newsubsetForm.field": function(){
        this.getProgram(this.newsubsetForm.field);
      },
      "newsubsetForm.program": function(){
        this.getcourses(this.newsubsetForm.program);
      },
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

.custom-select,
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

.custom-ul {
  width: 100%;
  max-height: 200px; 
  overflow-y: auto; 
}

input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

input[type="checkbox"]::before {
  content: '';
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 1px solid #ccc; 
  border-radius: 3px;
  background-color: #fff;
  vertical-align: middle;
  margin-right: 5px; 
}

input[type="checkbox"]:checked::before {
  background-color: #4CAF50;  
}
</style>
  