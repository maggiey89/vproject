<template>
  <div class="d-flex">
    <text>必修：2科6學分</text>
    <v-spacer/>
    <a href="https://www.mgt.ntnu.edu.tw/business-analysis">
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
        <tr v-for="item in compulsary" :key="item.name">
          <td width="300px">{{ item.id }}</td>
          <td width="300px">{{ item.name }}</td>
          <td>{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <text>選修：2科 6學分</text>
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
        compulsary: [
          {
            id: 'EEC8021',
            name: '企業管理與永續發展',
            credit: '3',
          },
          {
            id: 'O5C9007',
            name: '企業永續揭露與溝通議合',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'EEC8062',
            name: '永續金融',
            credit: '3',
          },
          {
            id: 'O5C9006',
            name: '企業ESG策略發展與治理',
            credit: '3',
          },
          {
            id: 'EEC8057',
            name: '碳管理',
            credit: '3',
          },
          {
            id: 'O5C9008',
            name: '永續應用專題',
            credit: '3',
          },
        ],
      }
    },
}

    </script>