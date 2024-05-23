<template>
  <div class="d-flex">
  <v-text>必修：4科12學分</v-text>
  <v-spacer/>
  <a href="https://www.ba.ntnu.edu.tw/%E6%9C%80%E6%96%B0%E6%B6%88%E6%81%AF-2"
    target="_blank" rel="noopener noreferrer"
  >
    <v-btn density="compact" variant="outlined" 
        style="color: black"
    >
    點我了解更多
    </v-btn>
  </a>  
  </div>  
    <v-table density="compact" fixed-header>
        <thead>
            <tr>
                <th class="text-left font-weight-bold">
                科目代碼
                </th>
                <th class="text-left font-weight-bold">
                科目名稱
                </th>
                <th class="text-left font-weight-bold">
                學分
                </th>
            </tr>
        </thead>
        <tbody>
        <tr v-for="item in course" :key="item.name" :class="{ 'textcolor': usercourses.includes(item.code) }">
            <td width="300px">{{ item.code }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <text>選修：2科6學分</text>
    <v-table density="compact" fixed-header>
        <thead>
            <tr>
                <th class="text-left font-weight-bold">
                科目代碼
                </th>
                <th class="text-left font-weight-bold">
                科目名稱
                </th>
                <th class="text-left font-weight-bold">
                學分
                </th>
            </tr>
        </thead>
        <!--tbody>
        <tr v-for="item in electives" :key="item.name">
            <td width="300px">{{ item.code }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
        </tr>
        </tbody-->
    </v-table>
</template>

<script>
import { getCurrentInstance } from 'vue';
import axios from 'axios';

  export default {
    data() {
      return {
        usercourses:[],
        course: [],
        subset: [],
        subsetcourse: [],
      }
    },

    methods: {
      async getcourses(){
        if(localStorage.getItem('user')){
          await this.getusercourses();
        }
        const path = 'http://127.0.0.1:5000/getsubset';
        const program = '基礎管理學分學程'
        axios.post(path, program)
        .then((res) => {
          this.course = res.data;
          for(var i = 0;i < this.course.length;i++){
            this.subset = this.course[i].courses;
            this.getcourseinfo(this.subset);
          }
          console.log(this.subsetcourse);
          //this.compulsary = this.courses.filter(course => course.type === 1)
          //this.electives = this.courses.filter(course => course.type === 0)
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getcourseinfo(c){
        const path = 'http://127.0.0.1:5000/getcoursesbycode';
        axios.post(path, {code: c})
        .then((res) => {
          this.subsetcourse.push(res.data);
        })
      },

      header() {
        const user = JSON.parse(localStorage.getItem('user'));
        if (user && user["access_token"]) {
          return { Authorization: `Bearer ${user["access_token"]}` };
        }
        else {
          return {};
        }
      },

      async getusercourses(){
        const path = 'http://127.0.0.1:5000/usercourses';
        axios.get(path, { headers: this.header() })
        .then((res) => {
          this.usercourses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      }
    },
    created(){
      this.getcourses();
    }
}

</script>

<style>
.textcolor {
  color: green;
}
</style>