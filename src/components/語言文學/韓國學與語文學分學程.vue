<template>
    <text>必修</text>
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
        <tr v-for="item in courses" :key="item.name">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <text>選修</text>
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
        <tr v-for="item in courses" :key="item.name">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
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
            id: 'L0U2001',
            name: '初級韓文(一)',
            credit: '2',
          },
          {
            id: 'L0U2002',
            name: '初級韓文(二)',
            credit: '2',
          },
          {
            id: 'L0U2003',
            name: '中級韓文(一)',
            credit: '2',
          },
          {
            id: 'L0U2004',
            name: '中級韓文(二)',
            credit: '2',
          },
          {
            id: 'L0U2005',
            name: '韓語會話與聽力練習（一）',
            credit: '2',
          },
          {
            id: 'L0U2006',
            name: '韓語會話與聽力練習（二）',
            credit: '2',
          },
          {
            id: 'L0U2022',
            name: '韓文閱讀與寫作',
            credit: '2',
          },
        ],
      }
    },
}

    </script>