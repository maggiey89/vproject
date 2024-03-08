<template>
    <!--v-container style="display: flex; justify-content: center; align-items: center; margin-top: 50px;">
    <v-form style="width: min(460px, 80%)">
        <v-text-field 
            label="科目代碼"
            variant="solo"
            append-inner-icon="mdi-plus"
            @click:append-inner="onClick"
        ></v-text-field>
    </v-form>    
    </v-container-->

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
    import ProfileNav from '@/components/Default/ProfileNav.vue'
</script>