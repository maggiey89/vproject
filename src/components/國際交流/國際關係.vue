<template>
  <div class="d-flex">
  <v-text>必修：2科6學分</v-text>
  <v-spacer/>
  <a href="http://www.deas.ntnu.edu.tw/front/Courses/Courses11/pages.php?ID=bnRudV9kZWFzJkNvdXJzZXMxMQ=="
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
    <text>選修：4科11學分</text>
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
            id: 'EAU0221',
            name: '近代外交史',
            credit: '3',
          },
          {
            id: 'EAC9003',
            name: '國際公法',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'L0U1001',
            name: '初級日文（一）',
            credit: '2',
          },
          {
            id: 'L0U2001',
            name: '初級韓文(一)',
            credit: '2',
          },
          {
            id: '0HUG502',
            name: '法語（一）',
            credit: '2',
          },
          {
            id: '0HUG503',
            name: '西班牙語（一）',
            credit: '2',
          },
          {
            id: '0HUG509',
            name: '泰語（一）',
            credit: '2',
          },
          {
            id: '0HUG649',
            name: '越南語（一）',
            credit: '2',
          },
          {
            id: '0HUG653',
            name: '印尼語（一）',
            credit: '2',
          },

          {
            id: 'EAU0124',
            name: '國際政治',
            credit: '3',
          },
          {
            id: 'EAU0220',
            name: '國際關係概論',
            credit: '3',
          },
          {
            id: 'EAU0194',
            name: '國際組織概論',
            credit: '3',
          },
          {
            id: 'EAU0113',
            name: '台灣外交研究',
            credit: '3',
          },
          {
            id: 'EAU0201',
            name: '中共對台政策與兩岸關係',
            credit: '3',
          },
          {
            id: 'EAU0206',
            name: '美國外交政策',
            credit: '3',
          },
          {
            id: 'EAU0229',
            name: '外交決策分析',
            credit: '3',
          },

          {
            id: 'GEU0057',
            name: '都市地理',
            credit: '3',
          },
          {
            id: 'GEU0006',
            name: '經濟地理',
            credit: '3',
          },
          {
            id: 'GEU0014',
            name: '世界地理',
            credit: '3',
          },
          {
            id: 'GEU0067',
            name: '歐洲地理',
            credit: '3',
          },
          {
            id: 'GEU0069',
            name: '亞洲地理',
            credit: '3',
          },
          {
            id: 'GEU0170',
            name: '自然資源保育',
            credit: '3',
          },
          {
            id: 'GEU0226',
            name: '環境永續',
            credit: '3',
          },
        ],
      }
    },
}

    </script>