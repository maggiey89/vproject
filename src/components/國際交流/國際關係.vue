<template>
  <div class="d-flex" style="margin-bottom: 10px;">
    <v-spacer/>
    <a href="http://www.deas.ntnu.edu.tw/front/Courses/Courses11/pages.php?ID=bnRudV9kZWFzJkNvdXJzZXMxMQ=="
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
      <template v-for="(each, index2) in subsetcourse">
        <v-data-table 
          v-if="index == index2"
          :headers="headers"
          fixed-header="true"
          :header-class="bold-header"
          :items="each"
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
    
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
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
        const path = 'http://127.0.0.1:5000/getsubset';
        //const path = 'http://127.0.0.1:5000/getcourses';
        const program = '基礎管理學分學程'
        //const program = '國際關係與外交學分學程'
        axios.post(path, program)
        .then((res) => {
          //this.course = res.data;
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

      deleteItem (item) {
        this.editedIndex = this.course.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.course.splice(this.editedIndex, 1)
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
  <v-text>必修：2科6學分</v-text>
  <v-spacer/>
  <a href="http://www.deas.ntnu.edu.tw/front/Courses/Courses11/pages.php?ID=bnRudV9kZWFzJkNvdXJzZXMxMQ=="
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
    <text>選修：4科11學分</text>
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
        courses: [
          {
            id: 'EAU0221',
            name: '近代外交史',
            credit: '3',
          },
          {
            id: 'EAC9003',
            name: '國際公法',
            credit: '3',
          },
        ],
        electives: [
          {
            id: 'L0U1001',
            name: '初級日文（一）',
            credit: '2',
          },
          {
            id: 'L0U2001',
            name: '初級韓文(一)',
            credit: '2',
          },
          {
            id: '0HUG502',
            name: '法語（一）',
            credit: '2',
          },
          {
            id: '0HUG503',
            name: '西班牙語（一）',
            credit: '2',
          },
          {
            id: '0HUG509',
            name: '泰語（一）',
            credit: '2',
          },
          {
            id: '0HUG649',
            name: '越南語（一）',
            credit: '2',
          },
          {
            id: '0HUG653',
            name: '印尼語（一）',
            credit: '2',
          },

          {
            id: 'EAU0124',
            name: '國際政治',
            credit: '3',
          },
          {
            id: 'EAU0220',
            name: '國際關係概論',
            credit: '3',
          },
          {
            id: 'EAU0194',
            name: '國際組織概論',
            credit: '3',
          },
          {
            id: 'EAU0113',
            name: '台灣外交研究',
            credit: '3',
          },
          {
            id: 'EAU0201',
            name: '中共對台政策與兩岸關係',
            credit: '3',
          },
          {
            id: 'EAU0206',
            name: '美國外交政策',
            credit: '3',
          },
          {
            id: 'EAU0229',
            name: '外交決策分析',
            credit: '3',
          },

          {
            id: 'GEU0057',
            name: '都市地理',
            credit: '3',
          },
          {
            id: 'GEU0006',
            name: '經濟地理',
            credit: '3',
          },
          {
            id: 'GEU0014',
            name: '世界地理',
            credit: '3',
          },
          {
            id: 'GEU0067',
            name: '歐洲地理',
            credit: '3',
          },
          {
            id: 'GEU0069',
            name: '亞洲地理',
            credit: '3',
          },
          {
            id: 'GEU0170',
            name: '自然資源保育',
            credit: '3',
          },
          {
            id: 'GEU0226',
            name: '環境永續',
            credit: '3',
          },
        ],
      }
    },
}

</script-->