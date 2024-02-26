// Composables
import { createRouter, createWebHistory } from 'vue-router'
/*
const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import( '@/views/Home.vue'),
        meta: {
          title: '首頁',
          //isAllowGuest: true,
        },
      },
    ],
  },
]
*/
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
      path: '/Language',
      name: '語言文學',
      component: () => import('@/components/語言文學/ViewPage.vue'),
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
