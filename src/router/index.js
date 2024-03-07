// Composables
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue'),
      meta: {
        title: '首頁',
        isAllowGuest: true,
      },
    },
    {
      path: '/Login',
      name: 'login',
      component: () => import('@/views/Login.vue'),
      meta: {
        title: '登入',
        isAllowGuest: true,
      },
    },
    {
      path: '/Upload',
      name: 'upload',
      component: () => import('@/views/Upload.vue'),
      meta: {
        title: '已修課程',
        isAllowGuest: true,
      },
    },
    {
      path: '/Language',
      name: '語言文學',
      component: () => import('@/components/語言文學/Language.vue'),
      meta: {
        title: '檢視',
        isAllowGuest: true,
      },
    },
    {
      path: '/International',
      name: '國際交流',
      component: () => import('@/components/國際交流/International.vue'),
      meta: {
        title: '檢視',
        isAllowGuest: true,
      },
    },
  ]
})

router.beforeEach((to, from) => {

  if (to.meta /*&& typeof to.meta.title === 'function'*/) {
    document.title = `${to.meta.title} | 國立臺灣師範大學`
  } else {
    document.title = '國立臺灣師範大學'
  }
})

export default router
