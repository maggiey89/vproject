<template>
  <div class="main-container">
    <!-- 左半部分：網站簡介 -->
    <div class="left-section">
      <v-text>歡迎來到我們的學分紀錄網站</v-text>
      <!-- 其他網站簡介內容... -->
      <div>
        <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1114">
        <v-btn style="color: black;">
          本校學分學程
        </v-btn>
      </a>
      </div>
      
    </div>

    <!-- 右半部分：圖片 -->
    <div class="right-section">
      <!-- <v-img src="Anya.jpg" alt="Website Image"></v-img> -->
    </div>
  </div>
</template>

<script setup>
import HelloWorld from "@/components/HelloWorld.vue";
</script>


<style scoped>
.main-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
}

.left-section {
  flex: 1;
  padding-right: 20px;
}

.right-section {
  flex: 1;
}
</style>

