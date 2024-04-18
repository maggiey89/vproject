<template>
    <div class="d-flex">
    <v-text>必修：6科 12學分</v-text>
    <v-spacer/>
    <a href="https://www.eng.ntnu.edu.tw/index.php/certificate-program/"
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
      <text>選修：3科 6學分</text>
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
              id: 'ENU5010',
              name: '主題式中級英語聽講',
              credit: '2',
            },
            {
              id: 'PGUK003',
              name: '英語口語溝通技巧',
              credit: '2',
            },
            {
              id: 'ENU5011',
              name: '英語溝通討論與思辯知能',
              credit: '2',
            },
            {
              id: 'ENU5012',
              name: '英語發表技巧',
              credit: '2',
            },
            {
              id: 'PGUK008',
              name: '英文專題報導',
              credit: '2',
            },
            {
              id: 'ENU5002',
              name: '情境式英語聽力練習',
              credit: '2',
            },
            {
              id: 'ENU5006',
              name: '進階英語聽講練習',
              credit: '2',
            },
            {
              id: 'ENU5008',
              name: '英語口語表達',
              credit: '2',
            },
          ],
          electives: [
            {
              id: 'ENU5013',
              name: '國際時事議題英文',
              credit: '2',
            },
            {
              id: 'PGUK004',
              name: '英文散文選讀',
              credit: '2',
            },
            {
              id: 'ENU5014',
              name: '英文寫作技巧：連貫性與銜接性',
              credit: '2',
            },
            {
              id: 'PGUK009',
              name: '中外文化議題探討',
              credit: '2',
            },
            {
              id: 'PGUK010',
              name: '翻譯入門',
              credit: '2',
            },
            {
              id: 'ENU0277',
              name: '中英翻譯（一）',
              credit: '2',
            },
            {
              id: 'ENU0278',
              name: '中英翻譯（二）',
              credit: '2',
            },
            {
              id: 'ENU5003',
              name: '互動式英語閱讀',
              credit: '2',
            },
            {
              id: 'ENU5007',
              name: '英美文學作品閱讀',
              credit: '2',
            },
            {
              id: 'ENU5009',
              name: '英語閱讀與寫作',
              credit: '2',
            },
          ],
        }
      },
  }
  
      </script>