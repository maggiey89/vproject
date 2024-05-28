<template>
  <div class="d-flex">
    <v-spacer/>
    <a href="https://www.ba.ntnu.edu.tw/%E6%9C%80%E6%96%B0%E6%B6%88%E6%81%AF-2"
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
          @click="deleteItem(index, item)"
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
        const program = '基礎管理學分學程'
        axios.post(path, program)
        .then((res) => {
          this.subset = res.data;
          for(var i = 0; i < this.subset.length;i++){
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
        this.deleteIndex = index
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
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
          this.deleteIndex = -1
        })
      },
    },

}

</script>
