<template>
    <div class="d-flex">
    <v-text>必修：1科 3學分</v-text>
    <v-spacer/>
    <a href="https://www.giti.ntnu.edu.tw/index.php/courses/pr/"
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
          <tr v-for="item in courses" :key="item.name">
            <td width="300px">{{ item.id }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
          </tr>
          </tbody>
      </v-table>
      <text>選修：3科 9學分</text>
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
            <td width="300px">{{ item.id }}</td>
            <td width="300px">{{ item.name }}</td>
            <td>{{ item.credit }}</td>
          </tr>
          </tbody>
      </v-table>
  </template>
  
  <script>
    export default {
      data() {
        return {
          courses: [
            {
              id: 'TIC9001',
              name: '基礎口筆譯入門',
              credit: '3',
            },
          ],
          electives: [
            {
              id: 'TIC9005',
              name: '中英口譯(一)',
              credit: '3',
            },
            {
              id: 'TIC9002',
              name: '中英筆譯(一)',
              credit: '3',
            },
            {
              id: 'TIC9004',
              name: '翻譯賞析',
              credit: '3',
            },
            {
              id: 'TIC9003',
              name: '中英口譯(二)',
              credit: '3',
            },
            {
              id: 'TIC9006',
              name: '中英筆譯(二)',
              credit: '3',
            },
          ],
        }
      },
  }
  
      </script>