<template>
  <v-card>
    <v-container>
      <h1>歡迎來到學分學程紀錄網站</h1>
      <div style="margin-top: 10px;">
        <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1114"
        target="_blank" rel="noopener noreferrer">
        <v-btn style="color: black;" variant="outlined">
          本校學分學程
        </v-btn>
      </a>
      </div>
    </v-container>
    
  <!--div class="main-container"-->
    <!-- 左半部分：網站簡介 -->
    <!--div class="left-section">
      <v-text>歡迎來到我們的學分紀錄網站</v-text-->
      <!-- 其他網站簡介內容... -->
      <!--div>
        <a href="https://www.cge.ntnu.edu.tw/article_d.php?lang=tw&tb=5&cid=114&id=1114"
        target="_blank" rel="noopener noreferrer">
        <v-btn style="color: black;">
          本校學分學程
        </v-btn>
      </a>
      </div>
      
    </div-->

    <!-- 右半部分：圖片 -->
    <!--div class="right-section">
      <v-img src="Anya.jpg" alt="Website Image"></v-img>
    </div>
  </div-->
</v-card>
</template>

<script setup>
import HelloWorld from "@/components/HelloWorld.vue";
</script>


<style scoped>
.v-card {
  background: url("@/assets/ntnubg.jpg") no-repeat center fixed;
  background-size: cover;
  width: 100%;
  height: 100%;
}
.v-container{
  background-color: rgb(248, 248, 247, 0.7);
  width: 50%;
  height: 150px; 
  margin-top: 200px; 
  text-align: center;
}
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

