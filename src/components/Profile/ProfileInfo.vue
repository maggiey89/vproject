<template>
  <div class="profile-container">
    <p class="profile-item"><strong>姓名：</strong>{{ profile.name }}</p>
    <p class="profile-item"><strong>信箱：</strong>{{ profile.email }}</p>
    <p class="profile-item"><strong>大學：</strong>{{ profile.university }}</p>
    <p class="profile-item"><strong>就讀科系：</strong>{{ profile.major }}</p>
    <p class="profile-item"><strong>身分：</strong>{{ profile.iden }}</p>
  </div>
</template>

<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 20px;
}

.profile-item {
  font-size: 16px;
  margin: 0;
  gap: 30px;
}
</style>

<script setup>
import ProfileNav from "@/components/Default/ProfileNav.vue";
// 從後端獲得使用者的個人資料
const profile = {
  name: "Bob Li",
  email: "xxxxxgmail.com",
  university: "台灣師範大學",
  major: "資訊工程學系",
  iden: "學生",
};
</script>