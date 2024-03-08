<template>
    <text>必修：4科 12學分</text>
    <v-table :headers="headers" :items="items">
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
            <td width="33%">{{ item.id }}</td>
            <td width="33%">{{ item.name }}</td>
            <td width="20%">{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <text>選修：2科 6學分</text>
    <v-table :headers="headers" :items="items">
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
            <td width="33%">{{ item.id }}</td>
            <td width="33%">{{ item.name }}</td>
            <td width="20%">{{ item.credit }}</td>
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
            id: 'PGUA006',
            name: '經濟學',
            credit: '3',
          },
          {
            id: 'PGUA007',
            name: '統計學',
            credit: '3',
          },
          {
            id: 'PGUA005',
            name: '	會計學',
            credit: '3',
          },
          {
            id: 'PGUA001',
            name: '企業概論',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'PGUA002',
            name: '管理學',
            credit: '3',
          },
          {
            id: 'PGUA004',
            name: '行銷管理',
            credit: '3',
          },
          {
            id: 'PGUA003',
            name: '財務管理',
            credit: '3',
          },
          {
            id: 'PGUA008',
            name: '資訊管理',
            credit: '3',
          },
          {
            id: 'PGUA009',
            name: '人力資源管理',
            credit: '3',
          },
          {
            id: 'PGUA011',
            name: '投資組合與個人財務分析',
            credit: '3',
          },
          {
            id: 'PGUA020',
            name: '餐旅產業管理',
            credit: '3',
          },
          {
            id: 'PGUA021',
            name: '產業分析',
            credit: '3',
          },
          {
            id: 'PGUA022',
            name: '策略管理',
            credit: '3',
          },
          {
            id: 'PGUA023',
            name: '投資學',
            credit: '3',
          },
          {
            id: 'PGUA024',
            name: '港台經商政治與社會文化',
            credit: '3',
          },
          {
            id: 'PGUA025',
            name: '基礎商業資料視覺化與溝通',
            credit: '3',
          },
          {
            id: '	BAU0006',
            name: '管理科學模式',
            credit: '3',
          },
        ],
      }
    },
}

</script>