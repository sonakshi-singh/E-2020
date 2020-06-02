import Vue from 'vue'
import Router from 'vue-router'
import DrugSearch from './components/DrugSearch.vue'
import KeyPhrases from './components/KeyPhrases.vue'
import FactSheet from './components/FactSheet.vue'
import Home from './components/Home.vue'
import Game from './components/Game_aak.vue'
import Upload from './components/upload.vue'
import Share from './components/share.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/keyPhrases',
      name: 'keyPhrases',
      component: KeyPhrases
    },
    {
      path: '/drugSearch',
      name: 'drugSearch',
      component: DrugSearch
    },
    {
      path: '/factSheet',
      name: 'factSheet',
      component: FactSheet
    },
    {
      path: '/Game',
      name: 'Game',
      component: Game
    },
    {
      path: '/upload',
      name: 'upload',
      component: Upload
    },
    {
      path: '/share',
      name: 'share',
      component: Share
    }

  ]
})
