import Router from 'vue-router'
import Login from '@/components/Login'
import Comics from '@/components/Comics'
//import App from '@/App'
import Vue from 'vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Login
    },
    {
      path: '/comics',
      component: Comics
    },
  ]
})
