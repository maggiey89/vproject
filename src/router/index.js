// Composables
import { createRouter, createWebHistory } from 'vue-router'

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
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
        meta: {
          title: '首頁',
          //isAllowGuest: true,
        },
      },
    ],
  },
]

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
