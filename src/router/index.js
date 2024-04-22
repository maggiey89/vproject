// Composables
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue'),
      meta: { title: '首頁', },
    },
    {
      path: '/course-view',
      name: 'courseview',
      component: () => import('@/views/CourseView.vue'),
      children: [
        {
          path: 'business',
          name: '商業管理',
          component: () => import('@/components/商業管理/Business.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'international',
          name: '國際交流',
          component: () => import('@/components/國際交流/International.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'leadership',
          name: '專業領導',
          component: () => import('@/components/專業領導/Leadership.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'education',
          name: '教育發展',
          component: () => import('@/components/教育發展/Education.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'culture',
          name: '文化創意',
          component: () => import('@/components/文化創意/Culture.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'socialscience',
          name: '社會科學',
          component: () => import('@/components/社會科學/SocialScience.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'tech',
          name: '科技應用',
          component: () => import('@/components/科技應用/Tech.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'language',
          name: '語言文學',
          component: () => import('@/components/語言文學/Language.vue'),
          meta: { title: '檢視', },
        },
        {
          path: 'information',
          name: '資訊應用',
          component: () => import('@/components/資訊應用/Information.vue'),
          meta: { title: '檢視', },
        },
      ],
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/register.vue'),
      meta: {
        title: '註冊',
        isAllowGuest: true,
      },
    },
    {
      path: '/login',
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
          path: 'mycourses',
          name: 'mycourses',
          component: () => import('@/components/Profile/MyCourses.vue'),
          meta: { title: '我的課程' },
        },
        {
          path: 'uploadcourse',
          name: 'uploadcourse',
          component: () => import('@/components/Profile/UploadCourse.vue'),
          meta: { title: '上傳課程' },
        },
      ],

    },
    {
      path: '/test',
      name: 'test',
      component: () => import('@/views/test.vue'),
      meta: { title: 'test', },
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('@/views/admin.vue'),
      meta: {
        title: '管理者',
        isAllowGuest: true,
      },
      children: [
        {
          path: '',
          name: 'showuser',
          component: () => import('@/components/admin/showuser.vue'),
          meta: { title: '數據顯示' },
        },
        {
          path: 'uploadcourse',
          name: 'adminuploadcourse',
          component: () => import('@/components/admin/uploadcourse.vue'),
          meta: { title: '上傳新課程' },
        },
        {
          path: 'uploadprogram',
          name: 'uploadprogram',
          component: () => import('@/components/admin/uploadprogram.vue'),
          meta: { title: '上傳新學程' },
        },
        {
          path: 'uploadfield',
          name: 'uploadfield',
          component: () => import('@/components/admin/uploadfield.vue'),
          meta: { title: '上傳新領域' },
        },
        {
          path: 'subset',
          name: 'subset',
          component: () => import('@/components/admin/subset.vue'),
          meta: { title: '上傳學程中分類' },
        },

      ],
    },
  ]
})

router.beforeEach((to, from) =>
{

  if (to.meta /*&& typeof to.meta.title === 'function'*/)
  {
    document.title = `${to.meta.title} | 國立臺灣師範大學`
  } else
  {
    document.title = '國立臺灣師範大學'
  }
})

export default router
