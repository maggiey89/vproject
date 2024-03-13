<template>

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