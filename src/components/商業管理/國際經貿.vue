<template>
  <div class="d-flex">
    <text>必修：3科9學分</text>
    <v-spacer/>
    <a href="https://www.mgt.ntnu.edu.tw/academic"
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
        <tr v-for="item in courses" :key="item.name" :class="{ 'textcolor': usercourses.includes(item.code) }">
          <td width="300px">{{ item.code }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <!--text>選修：1科 3學分</text>
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
        <tr v-for="item in electives" :key="item.name">
          <td width="300px">{{ item.code }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table-->
</template>

<script>
import { getCurrentInstance } from 'vue';
import axios from 'axios';

  export default {
    data() {
      return {
        usercourses:[],
        courses: [],
      }
    },

    methods: {
      async getcourses(){
        if(localStorage.getItem('user')){
          await this.getusercourses();
        }
        const path = 'http://127.0.0.1:5000/getcourses';
        const program = '國際經貿與涉外事務全英語學分學程'
        axios.post(path, program)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
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