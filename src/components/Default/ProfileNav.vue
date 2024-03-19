<template>
    <v-col cols="2" style="margin-left: 20px; text-align: left;">
      <v-list-item title="(姓名)" subtitle="選單"></v-list-item>
      <v-divider></v-divider>

    <router-link v-for="{name, route} in Categories" :to="{path: route}" style="text-decoration: none; color: inherit;">  
    <v-list-item>{{name}}</v-list-item>
    </router-link>  
    </v-col>
</template>

<script setup>
const Categories = [
    {name: '個人資料', route: '/profile'},
    {name: '我的課程', route: '/profile/mycourses'},
    {name: '新增課程', route: '/profile/uploadcourse'},
]
</script>