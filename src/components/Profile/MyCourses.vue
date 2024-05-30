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
        :items="course"
        :items-per-page="20"
        :search="search"
        density="compact"
    >
        <template v-slot:top >
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

        </template>
        <template v-if="headerfile.iden == 1 && isloggedin" v-slot:item.actions="{ item }">
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
        headerfile: {
            name: '',
            iden: '',
        },
        isloggedin: false,
        dialog: false,
        dialogDelete: false,
        codes: [],
        usercourses: [],
        headers: [
            { title: '科目代碼', key: 'code', align: 'start', width: '300px'},
            { title: '科目名稱', key: 'name', align: 'start', width: '300px'},
            { title: '學分', key: 'credit' },
            { title: '', key: 'actions', sortable: false},
        ],
        course: [
        {
            code: 'L0U1001',
            name: '初級日文（一）',
            credit: '2',
          },
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
/*
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
        async getcode() {
            const path = 'http://127.0.0.1:5000/usercourses';
            try {
            const res = await axios.get(path, { headers: this.header() });
            this.codes = res.data;
            } catch (error) {
            console.error(error);
            }
        },

        async getcourses() {
            await this.getcode();
            const path = 'http://127.0.0.1:5000/getcoursesbycode';
            const payload = {
            code: this.codes,
            };
            try {
            const res = await axios.post(path, payload);
            this.courses = res.data;
            } catch (error) {
            console.error(error);
            }
        }
    },
    created(){
        this.getcourses();
    },
}
*/
</script>
<style>
.v-data-table{
    text-align: left;
    padding-left: 20px;
    padding-right: 20px;
    height: max-content;
}
</style>