<template>
  <div class="d-flex" style="margin-bottom: 10px;">
    <v-text>必修：至少16學分</v-text>
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

  <v-data-table
    :headers="headers"
    fixed-header="true"
    :items="courses"
    :items-per-page="-1"
    density="compact"
  >
    <template v-slot:top >
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">確定要刪除此課程嗎？</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">取消</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">確認</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

    </template>
    <template v-if="headerfile.iden == 0 && isloggedin" v-slot:item.actions="{ item }">
      <v-icon
        size="small"
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template #bottom></template>
  </v-data-table>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      usercourses:[],
      courses: [],
      subset: [],
      subsetcourse: [],
      headerfile: {
        name: '',
        iden: '',
      },
      isloggedin: false,
      dialog: false,
      dialogDelete: false,
      headers: [
        { title: '科目代碼', key: 'code', align: 'start', width: '300px'},
        { title: '科目名稱', key: 'name', align: 'start', width: '300px'},
        { title: '學分', key: 'credit' },
        { title: '', key: 'actions', sortable: false},
      ],
      courses: [],
      editedIndex: -1,
      editedItem: {
        code: '',
        credit: '',
      },
      defaultItem: {
        code: '',
        name: '',
        credit: '',
      },
    }
  },

    watch: {
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      if (localStorage.getItem('user')) {
        this.isloggedin = true;
        this.getusercourses();
      }
      else{
        this.isloggedin = false;
      }
      this.getcourses();
    },

    methods: {
      header() {
        const user = JSON.parse(localStorage.getItem('user'));
        if (user && user["access_token"]) {
          return { Authorization: `Bearer ${user["access_token"]}` };
        }
        else {
          return {};
        }
      },

      async getusercourses(){
        const path = 'http://127.0.0.1:5000/usercourses';
        axios.get(path, { headers: this.header() })
        .then((res) => {
          this.usercourses = res.data;
          this.headerfile.name = res.data.name;
          this.headerfile.iden = res.data.iden;
        })
        .catch((error) => {
          console.error(error);
        });
      },
      
      async getcourses(){
        if(localStorage.getItem('user')){
          await this.getusercourses();
        }
        const path = 'http://127.0.0.1:5000/getcourses';
        const program = '國際關係與外交學分學程'
        axios.post(path, program)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getcourseinfo(c){
        const path = 'http://127.0.0.1:5000/getcoursesbycode';
        axios.post(path, {code: c})
        .then((res) => {
          this.subsetcourse.push(res.data);
        })
      },

      deleteItem (item) {
        this.editedIndex = this.courses.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.courses.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

    },
  }
</script>


<!--template>
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

</script-->