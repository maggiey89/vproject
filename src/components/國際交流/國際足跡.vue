<!--template>
  <div class="d-flex">
  <v-spacer/>
  <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1126"
    target="_blank" rel="noopener noreferrer"
  >
    <v-btn density="compact" variant="outlined" 
        style="color: black"
    >
    點我了解更多
    </v-btn>
  </a>  
  </div> 
  <template v-for="(subs, index) in subset">
    <v-text style="font-weight:bold">{{subs.name}}：{{subs.credit}}學分</v-text>
      <template v-for="(each, index2) in subsetcourse" >
        <v-table v-if="index == index2" density="compact" fixed-header>
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
                <th></th>
            </tr>
        </thead>
        <tbody>
          <template>
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
        <tr v-for="cs in each" :class="{'greentext': usercourses.includes(cs.code)}">
            <td width="300px">{{ cs.code }}</td>
            <td width="300px">{{ cs.name }}</td>
            <td>{{ cs.credit }}</td>
            <td ><v-icon
              v-if="headerfile.iden == 0 && isloggedin"
              size="small"
              @click="deleteItem(index2, cs)"
            > mdi-delete </v-icon></td>

        </tr>
        </tbody>
    </v-table>

      </template>

  </template>

</template>

<script>
import { getCurrentInstance } from 'vue';
import axios from 'axios';

  export default {
    data() {
      return {
        usercourses:[],
        course: [],
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
          { title: '學分', key: 'credit'},
          { title: '', key: 'actions', sortable: false},
        ],
        editedIndex: -1,
        deleteIndex: -1,
        editedItem: {
          code: '',
          name: '',
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
      dialog (val) {
        val || this.close()
      },
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
      this.getinfo();
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

      getinfo() {
        const path = 'http://127.0.0.1:5000/userinfo';
        axios.get(path, { headers: this.header() })
          .then((res) => {
            this.headerfile.name = res.data.name;
            this.headerfile.iden = res.data.iden;
          })
          .catch((error) => {
            console.error(error);
          });
      },

      async getusercourses(){
        const path = 'http://127.0.0.1:5000/usercourses';
        axios.get(path, { headers: this.header() })
        .then((res) => {
          this.usercourses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },
      
      async getcourses(){
        if(localStorage.getItem('user')){
          await this.getusercourses();
        }
        const path = 'http://127.0.0.1:5000/getsubset';
        const program = '國際關係與外交學分學程'
        axios.post(path, program)
        .then((res) => {
          this.subset = res.data;
          for(var i = 0;i < this.subset.length;i++){
            this.course = this.subset[i].courses;
            this.getcourseinfo(this.course);
          }
          console.log(this.subsetcourse);
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

      deleteItem (index, item) {
        this.editedIndex = this.subsetcourse[index].indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        this.deleteIndex = index
        console.log(item);
      },

      deleteItemConfirm () {
        this.subsetcourse[this.deleteIndex].splice(this.editedIndex, 1)
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

</script-->

<template>
  <div class="d-flex">
  <v-spacer/>
  <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1126"
    target="_blank" rel="noopener noreferrer"
  >
    <v-btn density="compact" variant="outlined" 
        style="color: black"
    >
    點我了解更多
    </v-btn>
  </a>  
  </div> 
  <v-text style="font-weight:bold">必修： 16學分</v-text>
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
            name: '［國外］赴外交換修習課程',
            credit: '6',
          },
          {
            id: '',
            name: '［國內］本校外語授課課程',
            credit: '10',
          },
          
        ],
        
      }
    },
}

</script>
