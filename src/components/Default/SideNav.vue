<template>
  <v-col cols="2" style="margin-left: 20px">
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
  {
    name: "商業管理",
    route: "/",
  },
  {
    name: "國際交流",
    route: "/International",
  },
  {
    name: "語言文學",
    route: "/Language",
  },
  {
    name: "科技應用",
    route: "/Technology",
  },
  {
    name: "資訊運用",
    route: "/Information",
  },
];
</script>