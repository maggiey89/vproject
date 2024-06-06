<template>
    <v-card>
      <template v-slot:text >
          <v-dialog v-model="dialogAdd" max-width="600px">
            <v-card>
              <v-card-title class="text-h5">新增課程</v-card-title>
              <v-autocomplete style="width: 500px" label="選擇課程"
                  :items="courseAdd" density="comfortable" variant="solo"
                  multiple chips closable-chips v-model="selectedItems" >ff
              </v-autocomplete>
                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="close">取消</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="save">儲存</v-btn>
                <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
          </v-dialog>
          
          <v-row>
            <v-text-field
            v-model="search"
            label="搜尋"
            append-inner-icon="mdi-magnify"
            variant="outlined"
            hide-details
            single-line
            density="compact"
            ></v-text-field>

            <v-btn @click="addItem()" style="color: blue;">新增課程</v-btn>
          </v-row>
        </template>

        <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
                <v-card-title class="text-h5">確定要刪除此課程嗎？</v-card-title>
                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue-darken-1" variant="text" @click="closeDelete">取消</v-btn>
                <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">確定</v-btn>
                <v-spacer></v-spacer>
                </v-card-actions>
            </v-card>
          </v-dialog>

        <v-data-table
        :headers="headers"
        fixed-header="true"
        :items="courses"
        :items-per-page="20"
        :search="search"
        density="compact"
        >

        <template v-slot:item.actions="{ item }">
        <v-icon
            size="small"
            @click="deleteItem(item)"
        >
            mdi-delete
        </v-icon>
        </template>
        <template #bottom></template>
    </v-data-table>
    </v-card>

</template>

<script>
import axios from 'axios';
export default {
    data() {
      return {
        codes: [],
        selectedItems: [],
        codeOnly: [],
        courses: [],
        usercourses: [],
        allCourses: [{code:'', name: '', credit: ''}],
        headers: [
            { title: '科目代碼', key: 'code', align: 'start', width: '300px'},
            { title: '科目名稱', key: 'name', align: 'start', width: '300px'},
            { title: '學分', key: 'credit' },
            { title: '', key: 'actions', sortable: false},
        ],
        search: '',
        headerfile: {
            name: '',
            iden: '',
        },
        isloggedin: false,
        dialogAdd: false,
        dialogDelete: false,
        editedIndex: -1,
        deletecode:'',
        addedCourse: {
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
      courseAdd(){
        return this.allCourses.map(course => course.code + " " + course.name + " " + course.credit);
      },
    },

    created () {
      if (localStorage.getItem('user')) {
        this.isloggedin = true;
        this.getinfo();
        this.getusercourses();
      }
      else{
        this.isloggedin = false;
      }
      this.getAllCourses();
    },

    watch: {
      usercourses: function(){
        this.getcourses();
      },
      dialogAdd (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
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
        })
        .catch((error) => {
          console.error(error);
        });
      },

      async getinfo() {
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
        const path = 'http://127.0.0.1:5000/getcoursesbycode';
        const ucourse = this.usercourses
        axios.post(path, {code : ucourse})
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      async getAllCourses(){
        const path = 'http://127.0.0.1:5000/getcourses';
        axios.get(path)
        .then((res) => {
          this.allCourses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      addcourse(codes){
        const path = 'http://127.0.0.1:5000/useraddcourse';
        axios.post(path, {course: codes}, {headers: this.header()})
        .then((res) => {
          if(res.data.success){
            console.log(res.data.success)
          }
        })
        .catch((error) => {
          console.error(error);
        });
      },

      deletecourse(code){
        const path = 'http://127.0.0.1:5000/userdeletecourse';
        axios.post(path, {course: code}, {headers: this.header()})
        .then((res) => {
          if(res.data.success){
            console.log(code)
          }
        })
        .catch((error) => {
          console.error(error);
        });
      },

      close () {
        this.dialogAdd = false
        this.$nextTick(() => {
          //this.addCourse = Object.assign({}, this.defaultItem)
          //this.editedIndex = -1
          this.selectedItems = []
          this.codeOnly = []
        })
      },

      
      save () {
        this.selectedItems.forEach(item => this.codeOnly.push(item.split(" ")[0]));
        //for (var i = 0; i < this.codeOnly.length; i++) {
          //if (!this.usercourses.has(this.codeOnly[i])) 
            //this.usercourses.push(codeOnly[i])
          
        //}
        this.addcourse(this.codeOnly);
        this.codeOnly.forEach(item => this.usercourses.push(item))
        //console.log(this.codeOnly)
        this.close();
        this.getcourses();
      },

      addItem () {
        this.dialogAdd = true
      },

      deleteItem (item) {
        this.editedIndex = this.usercourses.indexOf(item.code)
        this.dialogDelete = true
        this.deletecode = item.code
      },

      deleteItemConfirm () {
        this.usercourses.splice(this.editedIndex, 1)
        this.deletecourse(this.deletecode)
        this.deletecode = ''
        this.closeDelete()
        this.getcourses()
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedIndex = -1
        })
      },
    },
  }

</script>

<style scoped>
.v-card {
    margin-left: 10px;
    margin-right: 10px;
}
.v-text-field {
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 5px;
}
.v-btn {
    margin-top: 5px;
    margin-right: 10px;
}
</style>