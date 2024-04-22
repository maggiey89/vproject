<template>
    <div>
      <h1>新增小領域</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="field" class="custom-label">領域:</label>
          <select v-model="selectedField" id="field" class="custom-select">
            <option v-for="field in fields" :value="field.id">{{ field.name }}</option>
          </select>
        </div>
  
        <div class="form-group">
          <label for="program" class="custom-label">學程:</label>
          <select v-model="selectedProgram" id="program" class="custom-select">
            <option v-for="program in filteredPrograms" :value="program.id">{{ program.name }}</option>
          </select>
        </div>
  
        <h2>課程列表:</h2>
        <ul class="custom-ul">
          <li v-for="course in courses" :key="course.id">
            <label class="custom-label">
              <input type="checkbox" v-model="selectedCourses" :value="course.id">
              {{ course.name }}
            </label>
          </li>
        </ul>
  
        <div class="form-group">
          <label class="custom-label">必選或選修:</label>
          <input type="radio" id="compulsory" value="compulsory" v-model="selectionType">
          <label for="compulsory">必修</label>
          <input type="radio" id="elective" value="elective" v-model="selectionType">
          <label for="elective">選修</label>
        </div>
  
        <div v-if="selectionType === 'elective'" class="form-group">
          <label for="credits" class="custom-label">最低學分:</label>
          <input type="number" id="credits" v-model="minimumCredits" class="custom-input" placeholder="輸入數字">
        </div>
  
        <button type="submit" class="submit-button">確定</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        fields: [],
        programs: [],
        courses: [],
        selectedField: null,
        selectedProgram: null,
        selectedCourses: [],
        selectionType: 'compulsory',
        minimumCredits: null
      };
    },
    methods: {
      submitForm() {
        console.log({
          selectedField: this.selectedField,
          selectedProgram: this.selectedProgram,
          selectedCourses: this.selectedCourses,
          selectionType: this.selectionType,
          minimumCredits: this.minimumCredits
        });
      }
    },
    computed: {
      filteredPrograms() {
        return this.programs.filter(program => program.fieldId === this.selectedField);
      }
    },
    watch: {
      selectedField() {
        this.selectedProgram = null; // Reset selected program when changing field
      }
    },
    mounted() {
      this.fields = [
        { id: 1, name: '商業領域' },
        { id: 2, name: '國際交流領域' },
        // 其他領域...
      ];
      this.programs = [
        { id: 1, name: '基礎管理學分學程', fieldId: 1 },
        { id: 2, name: '財務金融學分學程', fieldId: 1 },
        { id: 3, name: '國際關係與外交學程', fieldId: 2 },
        { id: 4, name: '全英語學分學程', fieldId: 2 },
        // 其他學程...
      ];
      this.courses = [
        { id: 1, name: '課程A' },
        { id: 2, name: '課程B' },
        //
      // 其他課程...
      ];
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
  