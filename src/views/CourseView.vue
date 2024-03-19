<template>
    <v-container style="margin-top: 30px; height: 80px;">
      <v-row>
        <v-col/>
      <v-col style="text-align: center;"><h1>檢視</h1></v-col>
      <v-col>
        <v-form style="max-width: 200px; margin-left: 150px; ">
        <v-text-field 
            label="搜尋"
            variant="underlined"
            append-inner-icon="mdi-magnify"
            @click:append-inner="onClick"
        ></v-text-field>
        </v-form> 
      </v-col>
    </v-row>
    </v-container>
    <v-container style=" background-color: rgb(248, 248, 247); margin-bottom: 50px; height: 100%; ">
      <v-row no-gutters align="start">
      <SideNav/>
      <v-col style="margin-left: 40px; margin-right: 20px">

        <v-expansion-panels variant="accordion" style="display: flex; text-align: left; font-family: 'Noto Sans TC', serif;">
          <router-view/>
        </v-expansion-panels>

      </v-col>
    </v-row>
    </v-container>
  
</template>
  
<script setup>
  import SideNav from '@/components/Default/SideNav.vue'

</script>

<style>
.v-table {
    max-height: 300px;
}

</style>