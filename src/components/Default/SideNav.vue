<template>
  <v-col cols="2" style="margin-left: 20px; text-align: left;">
    <v-list-item title="學分學程" subtitle="選單"></v-list-item>
    <v-divider></v-divider>

    <router-link
      v-for="{ name, route } in Categories"
      :to="{ path: route }"
      style="text-decoration: none; color: inherit"
    >
      <v-list-item>{{ name }}</v-list-item>
    </router-link>
  </v-col>
</template>

<script setup>
const Categories = [
    {name: '商業管理', route: '/course-view'},
    {name: '國際交流', route: '/course-view/international'},
    {name: '專業領導', route: '/course-view'},
    {name: '教育發展', route: '/course-view'},
    {name: '文化創意', route: '/course-view'},
    {name: '社會科學', route: '/course-view'},
    {name: '科技應用', route: '/course-view'},
    {name: '語言文學', route: '/course-view/language'},
    {name: '資訊應用', route: '/course-view'},
]
</script>