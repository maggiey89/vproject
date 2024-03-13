<template>
    <text>必修：5科 10學分</text>
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
    <text>選修：2科 10學分</text>
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
            id: '',
            name: '大師創業管理入門',
            credit: '2',
          },
          {
            id: '',
            name: '大師創業論壇',
            credit: '2',
          },
          {
            id: '',
            name: '創業經營教戰手則',
            credit: '2',
          },
          {
            id: '',
            name: '誰是下一個賈伯斯 大師創業發想與實踐一',
            credit: '2',
          },
          {
            id: '',
            name: '誰是下一個賈伯斯 大師創業發想與實踐二',
            credit: '2',
          },
        ],
        electives: [
          {
            id: '',
            name: '',
            credit: '',
          },
          {
            id: '',
            name: '',
            credit: '',
          },
        ],
      }
    },
}

</script>