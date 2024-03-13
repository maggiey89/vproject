<template>
    <text>必修：1科 3學分</text>
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
        compulsary: [
          {
            id: 'BAU0066',
            name: '資料科學與管理決策',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'ITM0006',
            name: '高等統計學(一)',
            credit: '3',
          },
          {
            id: 'ISM0429',
            name: '資料庫管理研究',
            credit: '3',
          },
          {
            id: 'IAM0094',
            name: '資料探勘',
            credit: '3',
          },
          {
            id: 'IAM0101',
            name: '文字探勘',
            credit: '3',
          },
          {
            id: 'BAU0068',
            name: '商業分析程式語言',
            credit: '3',
          },
          {
            id: 'MBM0044',
            name: '資料庫行銷',
            credit: '3',
          },
          {
            id: 'MBM0094',
            name: '網路流量分析與行銷實務應用',
            credit: '3',
          },
          {
            id: 'MBM0092',
            name: '金融科技與應用',
            credit: '3',
          },
          {
            id: 'MBM0096',
            name: '商業資料視覺化設計與實務',
            credit: '3',
          },
        ],
      }
    },
}

</script>