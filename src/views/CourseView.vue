<template>
    <v-container style="margin-top: 30px; height: 80px; text-align: center; background-color: blanchedalmond;">
      <v-row>
        <v-col/>
      <v-col style="text-align: center;"><h1>檢視</h1></v-col>
      <v-col style="">
        <v-form style="width: min(200px, 80%); ">
        <v-text-field 
            label="科目代碼"
            variant="solo"
            append-inner-icon="mdi-plus"
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

        <v-expansion-panels variant="accordion" style="display: flex; font-family: 'Noto Sans TC', serif;">
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