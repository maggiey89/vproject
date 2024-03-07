<template>
    <text>必修：7科 14學分</text>
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
            <td width="33%">{{ item.id }}</td>
            <td width="33%">{{ item.name }}</td>
            <td width="20%">{{ item.credit }}</td>
        </tr>
        </tbody>
    </v-table>
    <text>選修：3科 6學分</text>
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
        electives: [
          {
            id: 'L0U2011',
            name: '韓語語法',
            credit: '2',
          },
          {
            id: 'L0U2012',
            name: '商用韓語',
            credit: '2',
          },
          {
            id: 'L0U2013',
            name: '韓國名著選讀',
            credit: '2',
          },
          {
            id: 'L0U2014',
            name: '韓國文化與現代生活',
            credit: '2',
          },
          {
            id: 'L0U2015',
            name: '現代韓國政治與經濟',
            credit: '2',
          },
          {
            id: 'L0U2016',
            name: '韓國學概論',
            credit: '2',
          },
          {
            id: 'L0U2017',
            name: '探索北韓',
            credit: '2',
          },
        ],
      }
    },
}

    </script>