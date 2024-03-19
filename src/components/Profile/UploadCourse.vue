<template>

    <v-form style="width: min(200px, 80%)">
        <v-text-field 
            label="科目代碼"
            variant="solo"
            append-inner-icon="mdi-plus"
            @click:append-inner="onClick"
        ></v-text-field>
    </v-form>    
  
</template>
    
<script setup>
    import { ref } from 'vue'
    //import { uid } from 'uid'
    //import { Icon } from '@iconify/vue'
    
    const todoList = ref([]);

    const fetchTodoList = () => {
        const savedTodoList = JSON.parse(localStorage.getItem("todoList", JSON.stringify(todoLIst.value)))
        if (savedTodoList) {
            todoList.value = savedTodoList;
        }
    };

    const setTodoListLocalStorage = () => {
        localStorage.setItem("todoList", JSON.stringify(todoLIst.value))
    };

    const createTodo = (todo) => {
        todoList.value.push({
            todo,
        });
    };
</script>