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
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <v-card>
            <v-card-title class="text-h5">編輯課程</v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    md="4"
                    sm="6"
                  >
                    <v-text-field
                      v-model="editedItem.id"
                      label="科目代碼"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    md="4"
                    sm="6"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="科目名稱"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    md="4"
                    sm="6"
                  >
                    <v-text-field
                      v-model="editedItem.credit"
                      label="學分"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">確定要刪除此課程嗎？</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

    </template>
    <template v-if="headerfile.iden == 0 && isloggedin" v-slot:item.actions="{ item }">
      <v-icon
        class="me-2"
        size="small"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
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
        id: '',
        name: '',
        credit: '',
      },
      defaultItem: {
        id: '',
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
        this.getinfo();
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

      async getcourses(){
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

      editItem (item) {
        this.editedIndex = this.courses.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
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

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.courses[this.editedIndex], this.editedItem)
        } else {
          this.courses.push(this.editedItem)
        }
        this.close()
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