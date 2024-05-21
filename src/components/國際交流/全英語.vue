<template>
  <div class="d-flex">
  <v-text>必修：至少20學分</v-text>
  <v-spacer/>
  <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1120"
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
    
</template>

<script>
  export default {
    data() {
      return {
        courses: [
          {
            id: '',
            name: '本校全英語通識課程',
            credit: '4',
          },
          {
            id: '',
            name: '全英語課程',
            credit: '16',
          },
          
        ],
        
      }
    },
}

</script>