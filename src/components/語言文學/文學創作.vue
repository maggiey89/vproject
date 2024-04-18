<template>
    <div class="d-flex">
    <v-text>選修：至少16學分</v-text>
    <v-spacer/>
    <a href="https://sites.google.com/view/ntnuchliterature/%E8%AA%B2%E7%A8%8B%E7%B0%A1%E4%BB%8B"
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
      <!--text>選修：3科 6學分</text>
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
      </v-table-->
  </template>
  
  <script>
    export default {
      data() {
        return {
          courses: [
            {
              id: 'CHU0015',
              name: '文學概論',
              credit: '3',
            },
            {
              id: 'CHU0074',
              name: '文學批評',
              credit: '3',
            },
            {
              id: 'CHU0324',
              name: '現代詩',
              credit: '2',
            },
            {
              id: 'CHU0325',
              name: '現代散文',
              credit: '2',
            },
            {
              id: 'CHU0326',
              name: '現代小說',
              credit: '2',
            },
            {
              id: 'CHU0035',
              name: '現代戲劇',
              credit: '3',
            },
            {
              id: 'PGUU016',
              name: '現代詩寫作指導',
              credit: '2',
            },
            {
              id: 'PGUU017',
              name: '現代散文寫作指導',
              credit: '2',
            },
            {
              id: 'PGUU018',
              name: '現代小說寫作指導',
              credit: '2',
            },
            {
              id: 'PGUU025',
              name: '現代劇本寫作指導',
              credit: '2',
            },
            {
              id: 'CHU0327',
              name: '成長小說（一）',
              credit: '2',
            },
            {
              id: 'CHU0328',
              name: '成長小說（二）',
              credit: '2',
            },
            {
              id: '',
              name: '旅行文學',
              credit: '2',
            },
            {
              id: '04UG021',
              name: '報導文學與紀錄片',
              credit: '3',
            },
            {
              id: 'CHU0134',
              name: '報導文學',
              credit: '3',
            },
            {
              id: 'CHU0179',
              name: '極短篇小說',
              credit: '2',
            },
            {
              id: 'PGUU029',
              name: '影像文學',
              credit: '2',
            },
            {
              id: 'PGUU028',
              name: '大眾小說寫作',
              credit: '2',
            },
            {
              id: 'CHU0339',
              name: '書法與身心紓發',
              credit: '2',
            },
            {
              id: 'CHU0344',
              name: '劇本寫作',
              credit: '2',
            },
            {
              id: 'CHU0340',
              name: '兒童文學',
              credit: '2',
            },
            {
              id: 'CHU0348',
              name: '媒體寫作',
              credit: '2',
            },
          ],
        }
      },
  }
  
      </script>