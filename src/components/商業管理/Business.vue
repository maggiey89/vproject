<template>
  <v-container style="margin-top: 50px; height: 100px; text-align: center; font-size: 30px;">
    檢視
  </v-container>
  <v-container style=" background-color: rgb(248, 248, 247); ">
    <v-row no-gutters align="start">
    <SideNav/>

    <v-col style="margin-left: 40px; margin-right: 20px">
      <v-expansion-panels variant="accordion" style="display: flex;">
        <v-expansion-panel v-for="{title, content} in Data">
          <v-expansion-panel-title expand-icon="mdi-menu-down">
            {{ title }}
          </v-expansion-panel-title>
          <v-expansion-panel-text>
            <Business/>
          </v-expansion-panel-text>
        </v-expansion-panel>

      </v-expansion-panels>
    </v-col>
  </v-row>
  </v-container>

</template>

<script setup>
import SideNav from '@/components/Default/SideNav.vue'
import Business from '@/components/商業管理/基礎管理學分學程.vue'
  const Data = [
    {
      title: '基礎管理學分學程',
      content: 'Business',
    },
    {
      title: '財務金融學分學程',
      content: 'blank',
    },
    {
      title: '大師創業學分學程',
      content: 'blank',
    },
    {
      title: '國際經貿與涉外事務全英語學分學程',
      content: 'blank',
    },
    {
      title: '商業分析學分學程',
      content: 'blank',
    },
    {
      title: 'ESG永續管理學分學程',
      content: 'blank',
    },

  ]
    
  //})
</script>