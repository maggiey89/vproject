<template>
    <div class="d-flex">
    <v-text>必修：9科 18學分</v-text>
    <v-spacer/>
    <a href="https://www.cla.ntnu.edu.tw/index.php/japanese-program-enrollment/"
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
      <text>選修：1科 2學分</text>
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
              id: 'L0U1001',
              name: '初級日文(一)',
              credit: '2',
            },
            {
              id: 'L0U1002',
              name: '初級日文(二)',
              credit: '2',
            },
            {
              id: 'L0U1003',
              name: '中級日文(一)',
              credit: '2',
            },
            {
              id: 'L0U1004',
              name: '中級日文(二)',
              credit: '2',
            },
            {
              id: 'L0U1005',
              name: '日語會話與聽講（一）',
              credit: '2',
            },
            {
              id: 'L0U1006',
              name: '日語會話與聽講（二）',
              credit: '2',
            },
            {
              id: 'L0U1009',
              name: '進階日文（一）',
              credit: '2',
            },
            {
              id: 'L0U1010',
              name: '進階日文（二）',
              credit: '2',
            },
            {
              id: 'L0U1019',
              name: '日文閱讀與寫作',
              credit: '2',
            },
          ],
          electives: [
            {
              id: 'L0U1014',
              name: '日本歷史',
              credit: '2',
            },
            {
              id: 'L0U1013',
              name: '日本文化史',
              credit: '2',
            },
            {
              id: 'L0U1015',
              name: '日本文學史',
              credit: '2',
            },
            {
              id: 'L0U1018',
              name: '新聞日語',
              credit: '2',
            },
            {
              id: 'L0U1017',
              name: '商用日文',
              credit: '2',
            },
            {
              id: 'L0U1016',
              name: '日本文學名著選讀',
              credit: '2',
            },
            {
              id: 'L0U1011',
              name: '進階日語會話與聽講(一)',
              credit: '2',
            },
            {
              id: 'L0U1012',
              name: '進階日語會話與聽講(二)',
              credit: '2',
            },
          ],
        }
      },
  }
  
      </script>