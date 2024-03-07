<template>
    <text>必修：3科 9學分</text>
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
    <text>選修：1科 3學分</text>
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
            id: 'O5C9005',
            name: '全球經濟與機遇',
            credit: '3',
          },
          {
            id: 'EAU0139',
            name: '跨國企業經營策略',
            credit: '3',
          },
          {
            id: 'E0C9009',
            name: '智慧財產權法專題研究',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'O5C9004',
            name: '跨國企業併購談判',
            credit: '3',
          },
          {
            id: 'EAU0204',
            name: '韓半島政治與經濟',
            credit: '3',
          },
          {
            id: 'E0C9010',
            name: '國際金融專題研究',
            credit: '3',
          },
        ],
      }
    },
}

</script>