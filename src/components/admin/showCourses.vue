<template>
    <v-card>
        <template v-slot:text>
        <v-text-field
            v-model="search"
            label="搜尋"
            append-inner-icon="mdi-magnify"
            variant="outlined"
            hide-details
            single-line
            density="compact"
        ></v-text-field>
        </template>
        <v-data-table
        :headers="headers"
        fixed-header="true"
        :items="courses"
        :items-per-page="20"
        :search="search"
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
                        v-model="editedItem.code"
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
    </v-data-table>
    </v-card>
</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      search: '',
      headerfile: {
        name: '',
        iden: '',
      },
      isloggedin: false,
      dialog: false,
      dialogDelete: false,
      deletecode: '',
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
        if(localStorage.getItem('user')){
          await this.getusercourses();
        }
        const path = 'http://127.0.0.1:5000/getcourses';
        axios.get(path)
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
        console.log(this.editedItem)
        this.close()
      },
    },
  }
</script>

<style>
.v-data-table{
    text-align: left;
    padding-left: 20px;
    padding-right: 20px;
    height: max-content;
}
</style>