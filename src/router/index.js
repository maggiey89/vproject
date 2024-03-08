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
      path: '/course-view',
      name: 'courseview',
      component: () => import('@/views/CourseView.vue'),
      children: [
        {
          path: '',
          name: '商業管理',
          component: () => import('@/components/商業管理/Business.vue'),
          meta: {
            title: '檢視',
            isAllowGuest: true,
          },
        },
        {
          path: 'international',
          name: '國際交流',
          component: () => import('@/components/國際交流/International.vue'),
          meta: {
            title: '檢視',
            isAllowGuest: true,
          },
        },
        {
          path: 'language',
          name: '語言文學',
          component: () => import('@/components/語言文學/Language.vue'),
          meta: {
            title: '檢視',
            isAllowGuest: true,
          },
        },
      ],
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
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/Profile.vue'),
      children: [
        {
          path: '',
          name: 'profileinfo',
          component: () => import('@/components/Profile/ProfileInfo.vue'),
          meta: { title: '個人資料' },
        },
        {
          path: 'uploadcourse',
          name: 'uploadcourse',
          component: () => import('@/components/Profile/UploadCourse.vue'),
          meta: { title: '上傳課程' },
        },
      ],
      
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
