<template>
  <div>
    <v-card class="top-section">
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
    </v-card>

    <main class="main-content">
      <section class="text">
        <h2>網站介紹</h2>
      </section>
      <section class="picture">
        <div class="item">
          <img src="" alt="cp2" class="circle-img">
          <h3>即時學程追蹤</h3>
        </div>
        
        <div class="item">
          <img src="" alt="cp3" class="circle-img">
          <h3>個人化學程管理</h3>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import HelloWorld from "@/components/HelloWorld.vue";
</script>

<style scoped>
.top-section {
  background: url("@/assets/ntnubg.jpg") no-repeat center center fixed; /* 固定背景 */
  background-size: cover;
  width: 100%;
  height: 100vh;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.v-container {
  background-color: rgba(248, 248, 247, 0.8); 
  width: 50%;
  padding-top: 10px;
  padding-bottom: 20px;
  text-align: center;
  border-radius: 15px; 
}

.main-content {
  background-color:trans; 
  padding: 50px 0;
  text-align: center;
}

.picture {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 20px;
}

.item {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black; 
}

.circle-img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

h1, h2, h3, p {
  margin: 10px 0;
  color: black;
}
</style>
