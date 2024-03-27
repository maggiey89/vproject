<template>
    <v-form style="width: min(200px, 80%)" >
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
    if (courseState.course !== ""){
        emit("create-course", courseState.course);
        courseState.course = "";
        return;
    }
    courseState.invalid = true;
    courseState.errMsg = "Value cannot be empty";
};

</script>

<style>
.input-wrap{
    display: flex;
    transition: 250ms ease;
    border: 2px solid #41b080;
}
</style>