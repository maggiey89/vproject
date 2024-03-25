<template>
  <div class="d-flex">
    <text>必修：5科14學分</text>
    <v-spacer/>
    <a href="https://sites.google.com/view/ntnufin/"
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
            id: 'CEU0439',
            name: '會計學',
            credit: '3',
          },
          {
            id: 'CEU0512',
            name: '統計學概論',
            credit: '3',
          },
          {
            id: 'CEU0011',
            name: '經濟學',
            credit: '2',
          },
          {
            id: 'CEU0076',
            name: '貨幣銀行學',
            credit: '3',
          },
          {
            id: 'CEU0313',
            name: '國際金融',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'PGUB005',
            name: '管理學',
            credit: '3',
          },
          {
            id: 'CEU0493',
            name: '財務報表分析',
            credit: '3',
          },
          {
            id: 'CEU0317',
            name: '投資學',
            credit: '3',
          },
          {
            id: 'CEU0399',
            name: '財務管理',
            credit: '3',
          },
          {
            id: 'CEU0494',
            name: '金融市場',
            credit: '3',
          },
          {
            id: 'CEU0496',
            name: '產業分析',
            credit: '3',
          },
          {
            id: 'PGUB013',
            name: '財務數學',
            credit: '3',
          },
          {
            id: 'PGUB014',
            name: '期貨與選擇權',
            credit: '3',
          },
          {
            id: 'PGUB015',
            name: '計量財務分析',
            credit: '3',
          },
        ],
      }
    },
}

    </script>