<template>
    <div class="admin-buttons">
      <button @click="openAnalytics">數據分析</button>
      <button @click="openAddCourse">上架課程</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      openAnalytics() {
        // 在這裡實現數據分析功能，例如導航到數據分析頁面
        console.log('執行數據分析功能');
      },
      openAddCourse() {
        // 在這裡實現上架課程功能，例如導航到上架課程頁面
        console.log('執行上架課程功能');
      }
    }
  }
  </script>
  
  <style>
  .admin-buttons {
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 999; /* 將 z-index 設置為較高的值 */
}

  .admin-buttons button {
    margin-right: 10px;
  }
  </style>
  