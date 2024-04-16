<template>
   
    <v-form style="width: 200px; height: 50px; margin-bottom: 20px;" >
        <v-text-field 
            label="科目代碼"
            variant="underlined"
            v-model="courseState.course"
            append-inner-icon="mdi-plus"
            @click:append-inner="createcourse()"
        ></v-text-field>
    </v-form> 
    
    <div style="text-align: left; font-size: 12px;" >{{ courseState.errMsg }}</div>

</template>

<script setup>
import {reactive, defineEmits} from 'vue'

const emit = defineEmits(["create-course"])

const courseState = reactive({
    course: "",
    invalid: null,
    errMsg: "",
})

const createcourse = () => {
    courseState.invalid = null;
    if (courseState.course == ""){
        courseState.invalid = true;
        courseState.errMsg = "Value cannot be empty";
        return;
    }
    if (courseState.course.length != 7) {
        courseState.invalid = true;
        courseState.errMsg = "科目代碼錯誤";
        return;
    } 
    
    emit("create-course", courseState.course);
    courseState.course = "";
};

/*export default {
    
    methods: {
    header(){
        const user = JSON.parse(localStorage.getItem('user'));
        if(user && user["access_token"]){
            return {Authorization : `Bearer ${user["access_token"]}`};
        } else {
            return {};
        }
    },

    postcourse(){
        const path = 'http://127.0.0.1:5000/useraddcourse';
        axios.post(path, { headers : header(), course : courseState.course })
        .then((response) => console.log(response))
        .catch((error) => console.log(error))
    },
    }
}*/


</script>

<style>

</style>