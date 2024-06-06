<template>
    <v-container>
      <v-file-input
        label="請上傳CSV檔案"
        accept=".csv"
        v-model="file"
        show-size
        chips
      ></v-file-input>
      <v-btn @click="submitFile">upload</v-btn>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        file: null,
      };
    },
    methods: {
      submitFile() {
        if (this.file) {
          const fileName = this.file.name;
          if (fileName.endsWith('.csv')) {
            alert('文件上傳成功：' + fileName);
            // 看要怎麼處理；；
          } else {
            alert('請上傳CSV格式的文件');
          }
        } else {
          alert('請選擇文件');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .v-container {
    margin-top: 20px;
  }
  </style>
  