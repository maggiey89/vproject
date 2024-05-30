<template>

    <CourseCreator @create-course="createCourse"/>
    
    <CourseItems v-for="(course, index) in courseList" 
        :course="course" 
        :index="index"
        @edit-course="toggleEditCourse"
        @update-course="updateCourse"
        @delete-course="deleteCourse"
    />
    
    <!--v-data-table
    :headers="headers"
    fixed-header="true"
    :items="courseList"
    :items-per-page="-1"
    density="compact"
  >
    <template v-slot:top >
        <v-spacer></v-spacer>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

    </template>
    <template v-slot:item.actions="{ item }">
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
  </v-data-table-->
    
</template>
    
<script setup>
import CourseCreator from './CourseCreator.vue'
import CourseItems from './CourseItems.vue'
import { ref, watch } from 'vue'
import { v4 as uuidv4 } from "uuid"

const headers = [
    { title: '科目代碼', key: 'code', align: 'start', width: '300px'},
    { title: '科目名稱', key: 'name', align: 'start', width: '300px'},
    { title: '學分', key: 'credit' },
    { title: '', key: 'actions', sortable: false},
]
const courseList = ref([]);

watch(
    courseList, 
    () => {
        setcourseListLocalStorage();
    },
    {
        deep: true,
    }
);

const fetchcourseList = () => {
    const savedcourseList = JSON.parse(localStorage.getItem("courseList", JSON.stringify(courseList.value))) 
    if (savedcourseList) {
        courseList.value = savedcourseList;
    }
};

fetchcourseList();

const setcourseListLocalStorage = () => {
    localStorage.setItem("courseList", JSON.stringify(courseList.value))
};

const createCourse = (course) => {
    courseList.value.push({
        id: uuidv4(), 
        course,
        isCompleted: null,
        isEditing: null,
    });
};

const toggleEditCourse = (coursePos) => {
    courseList.value[coursePos].isEditing = !courseList.value[coursePos].isEditing;
};

const updateCourse = (courseVal, coursePos) => {
    courseList.value[coursePos].course = courseVal;
};

const deleteCourse = (courseId) => {
    courseList.value = courseList.value.filter((course) => course.code != courseId);
};

</script>

<style>
.v-select{
    width: 200px; 
    height: 50px; 
    margin-bottom: 20px;
}
</style>