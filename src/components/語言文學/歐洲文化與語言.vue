<template>
    <div class="d-flex">
    <v-text>歐洲文化領域：2科 6學分</v-text>
    <v-spacer/>
    <a href="https://www.giect.ntnu.edu.tw/index.php/programintroduction/"
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
      <text>歐洲語言領域：3科 6學分</text>
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
              id: '',
              name: '歐洲文化史',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲文學概論',
              credit: '3',
            },
            {
              id: '',
              name: '語言與文化',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲文化創意',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲電影史',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲文化遺產與觀光',
              credit: '3',
            },
            {
              id: '',
              name: '20世紀文學、音樂、藝術與電影',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲地理文化的幻想與相遇',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲藝術名作閱讀',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲神話',
              credit: '3',
            },
            {
              id: '',
              name: '歐洲奇幻文學',
              credit: '3',
            },
            {
              id: '',
              name: '現代歐陸哲學選讀',
              credit: '3',
            },
          ],
          electives: [
            {
              id: '',
              name: '法文（一）',
              credit: '3',
            },
            {
              id: '',
              name: '德文（一）',
              credit: '3',
            },
            {
              id: '',
              name: '西班牙文（一）',
              credit: '3',
            },
            {
              id: '',
              name: '拉丁文（一）',
              credit: '3',
            },
            {
              id: '',
              name: '法文（二）',
              credit: '3',
            },
            {
              id: '',
              name: '德文（二）',
              credit: '3',
            },
            {
              id: '',
              name: '西班牙文（二）',
              credit: '3',
            },
            {
              id: '',
              name: '拉丁文（二）',
              credit: '3',
            },
            {
              id: '',
              name: '法文（三）',
              credit: '3',
            },
            {
              id: '',
              name: '德文（三）',
              credit: '3',
            },
            {
              id: '',
              name: '西班牙文（三）',
              credit: '3',
            },
            {
              id: '',
              name: '法文（四）',
              credit: '3',
            },
            {
              id: '',
              name: '德文（四）',
              credit: '3',
            },
            {
              id: '',
              name: '西班牙文（四）',
              credit: '3',
            },
          ],
        }
      },
  }
  
      </script>