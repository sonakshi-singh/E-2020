import Vue from 'vue'
import Router from 'vue-router'

import login from './components/Login.vue'
import upload from './components/upload.vue'
import share from './components/share.vue'
import templatePage from './components/templatePage.vue'
import gallery from './components/gallery.vue'
import home from './components/home.vue'
import collab from './components/collab.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/gallery',
      name: 'gallery',
      component: gallery
    },
    {
      path: '/templatePage',
      name: 'templatePage',
      component: templatePage
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload
    },
    {
      path: '/share',
      name: 'share',
      component: share
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/collab',
      name: 'collab',
      component: collab
    },

  ]
})
