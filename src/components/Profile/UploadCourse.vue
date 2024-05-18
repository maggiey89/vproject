<template>
  
    

    <CourseCreator @create-course="createCourse"/>
    
    <CourseItems v-for="(course, index) in courseList" 
        :course="course" 
        :index="index"
        @edit-course="toggleEditCourse"
        @update-course="updateCourse"
        @delete-course="deleteCourse"
    />
    
    
</template>
    
<script setup>
import CourseCreator from './CourseCreator.vue'
import CourseItems from './CourseItems.vue'
import { ref, watch } from 'vue'
import { v4 as uuidv4 } from "uuid"

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
    courseList.value = courseList.value.filter((course) => course.id != courseId);
};

</script>

<style>
.v-select{
    width: 200px; 
    height: 50px; 
    margin-bottom: 20px;
}
</style>