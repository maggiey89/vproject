<template>
    <div>
        <v-autocomplete label="領域" v-model="editProgram.field" id="field" 
            required :items="fields" density="comfortable" variant="solo">
        </v-autocomplete>

        <v-autocomplete label="學程" v-model="editProgram.program" id="program" 
            required :items="programs" density="comfortable" variant="solo">
        </v-autocomplete>
        
        <v-autocomplete label="課程分類" v-model="editProgram.subset" id="subset" 
            :items="subsettitle" density="comfortable" variant="solo">
        </v-autocomplete>

        
    </div>
    <v-card>
        <template v-slot:text v-model="editProgram.name">
          <v-dialog v-model="dialogAdd" max-width="600px">
            <v-card>
              <v-card-title class="text-h5">新增課程</v-card-title>
              <v-autocomplete style="width: 500px" label="選擇課程" v-model="addedCourse.add" id="add"
                  :items="courseAdd" density="comfortable" variant="solo">
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

            <v-btn @click="addItem(add)">新增課程</v-btn>
          </v-row>
        </template>
        
            <v-spacer></v-spacer>
                
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
                :items="computedCourses"
                :items-per-page="20"
                :search="search"
                density="compact"
            >
            
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

    </v-card>

    <v-dialog v-model="dialogDeleteProgram" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">確定要刪除此學分學程嗎？</v-card-title>
        <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue-darken-1" variant="text" @click="closeDelete">取消</v-btn>
        <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">確定</v-btn>
        <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-btn style="margin-top: 20px; color: red" @click="deleteProgram(program)">刪除此學分學程</v-btn>
    
</template>
  
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        fields: [],
        programs: [],
        subset: [],
        subsettitle: [],
        subsetcourse: [],
        courses: [],
        allCourses: [{code:'', name: '', credit: ''}],
        chosesubset: false,
        editProgram:{
          field: '',
          program: '',
          subset: '',
          name: '',
          course: [],
          credit: 0,
        },
        search: '',
      headerfile: {
        name: '',
        iden: '',
      },
      isloggedin: false,
      dialogAdd: false,
      dialogDelete: false,
      dialogDeleteProgram: false,
      deletecode: '',
      headers: [
        { title: '科目代碼', key: 'code', align: 'start', width: '300px'},
        { title: '科目名稱', key: 'name', align: 'start', width: '300px'},
        { title: '學分', key: 'credit' },
        { title: '', key: 'actions', sortable: false},
      ],
      subIndex: -1,
      editedIndex: -1,
      addedCourse: {
        code: '',
        name: '',
        credit: '',
      },
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
      };
    },

    computed: {
      computedCourses() {
        return this.editProgram.subset ? this.subsetcourse[this.subIndex] : this.courses;
      },
      courseAdd() {
        return this.allCourses.map(course => course.code + " " + course.name + " " + course.credit);
      },
    },

    created(){
      if (localStorage.getItem('user')) {
        this.isloggedin = true;
        this.getinfo();
      }
      else{
        this.isloggedin = false;
      }
      this.getcourses();
      this.getinfo();
      this.getFields();
      this.getAllCourses();
    },

    watch: {
      "editProgram.field": function(){
        this.getProgram(this.editProgram.field);
      },
      "editProgram.program": function(){
        this.getSubset(this.editProgram.program);
        this.getcourses(this.editProgram.program);
      },
      "editProgram.subset": function(){
        this.getsubsetcourses(this.editProgram.program, this.editProgram.subset);
        this.chosesubset = true;
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
      
      getFields(){
        const path = 'http://127.0.0.1:5000/getfield';
        axios.get(path)
        .then((res) => {
          this.fields = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getProgram(f){
        const path = 'http://127.0.0.1:5000/getprogram';
        axios.post(path, f)
        .then((res) => {
          this.programs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getSubset(p){
        const path = 'http://127.0.0.1:5000/getsubset';
        const program = p;
        axios.post(path, program)
        .then((res) => {
          this.subset = res.data;
          for(var i = 0; i < this.subset.length;i++){
            this.course = this.subset[i].courses;
            this.getcourseinfo(this.course);
            this.subsettitle.push(this.subset[i].name);
          }
          console.log(this.subsetcourse);
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getsubsetcourses(p, s) {
        const path = 'http://127.0.0.1:5000/getsubset';
        const program = p;
        axios.post(path, program)
        .then((res) => {
          this.subset = res.data;
          for(var i = 0; i < this.subset.length;i++){
            if (this.subset[i].name.includes(s))
                this.subIndex = i;
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

      getcourses(p){
        const path = 'http://127.0.0.1:5000/getcourses';
        const program = p;
        axios.post(path, program)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
      },

      getAllCourses(){
        const path = 'http://127.0.0.1:5000/getcourses';
        axios.get(path)
        .then((res) => {
          this.allCourses = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
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

      close () {
        this.dialogAdd = false
        this.$nextTick(() => {
          this.addCourse = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        this.courses.push(this.addedCourse)
        console.log(this.addedCourse)
        this.close()
      },

      addItem (item) {
        //this.editedIndex = this.courses.indexOf(item)
        //this.editedItem = Object.assign({}, item)
        this.addedCourse = Object.assign({},this.addedCourse.add)
        this.dialogAdd = true
      },
/*
      deleteItem (item) {
        this.editedIndex = this.courses.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        this.deletecode = item.code
      },

      deleteItemConfirm () {
        const path = 'http://127.0.0.1:5000/deletecourse';
        const code = this.deletecode;
        axios.post(path, code)
        .then((res) => {
          if(res.data.success){
            alert("已刪除課程。")
          }
        })
        .catch((error) => {
          console.error(error);
        })
        this.courses.splice(this.editedIndex, 1)
        this.closeDelete()
      },
*/
    deleteItem (item) {
        this.editedIndex = this.computedCourses.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        console.log(item);
      },

      deleteItemConfirm () {
        this.computedCourses.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      closeDelete () {
        this.dialogDelete = false
        this.dialogDeleteProgram = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      deleteProgram(program) {
        this.dialogDeleteProgram = true
      }
    },
};
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
  