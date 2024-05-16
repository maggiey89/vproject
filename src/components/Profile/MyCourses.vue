<template>

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
            <tr v-for="item in codes" >
            <td width="300px">{{ item }}</td>
        </tr>
        </tbody>
    </v-table>

</template>

<script>
import axios from 'axios';
export default {
    data() {
      return {
        codes: [],
        courses: [],
      };
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
        getcode(){
            const path = 'http://127.0.0.1:5000/usercourses';
            axios.get(path, { headers: this.header() })
            .then((res) => {
                this.codes = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        },
        getcourses(){
            this.getcode();
            /*const path = 'http://127.0.0.1:5000/getonecourse';
            
            axios.get(path, { headers: this.header() })
            .then((res) => {
                this.codes = res.data;
            })
            .catch((error) => {
                console.error(error);
            });*/
        }
    },
    created(){
        this.getcourses();
    }
}

</script>