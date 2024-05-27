<template>
    <v-container style="margin-top: 30px; height: 100px; text-align: center;">
      <h1>{{$route.meta.title}}</h1>
    </v-container>
    <v-container style=" background-color: rgb(248, 248, 247); margin-bottom: 50px; height: 100%;">
      <v-row no-gutters align="start">
      <ProfileNav/>
  
      <v-col style="margin-left: 40px; margin-right: 20px">
        <router-view/>
      </v-col>
    </v-row>
    </v-container>
  
</template>
    
<script setup>
import ProfileNav from '@/components/Default/ProfileNav.vue'

</script>