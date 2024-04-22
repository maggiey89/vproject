<template>
    <v-col cols="2" style="margin-left: 20px; text-align: left;">
      <v-list-item>{{ adminName }}</v-list-item>
      <v-divider></v-divider>
  
      <router-link v-for="{ name, route } in AdminCategories" :to="{ path: route }" style="text-decoration: none; color: inherit;">
        <v-list-item>{{ name }}</v-list-item>
      </router-link>
    </v-col>
  </template>
  
  <script setup>
  import { ref } from 'vue'; 
  
  const AdminCategories = [
      { name: '數據顯示', route: '/admin/' },
      { name: '新增課程', route: '/admin/uploadcourse' },
      { name: '新增學程', route: '/admin/uploadprogram' },
      { name: '新增領域', route: '/admin/uploadfield' },
      { name: '新增學程中分類', route: '/admin/subset' },
  ];
  const adminAvatar = ref('url_to_default_avatar'); 
  const adminName = ref(''); 
  
  const fetchAdminInfo = () => {
    const adminInfo = {
      avatar: 'url_to_admin_avatar',
      name: 'Adminstrator' 
    };
  
    adminAvatar.value = adminInfo.avatar;
    adminName.value = adminInfo.name;
  };
  
  fetchAdminInfo();
  </script>
  