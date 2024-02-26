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
      }
    },
}

    </script>