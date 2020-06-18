import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Registered from '../views/Registered.vue'
import Fibit_access from '../views/Fibit_access'
import Manage_data from '../views/Manage_data'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Registered',
    name: 'Registered',
    component: Registered
  },
  {
    path: '/fibit_access/',
    name: 'Fibit_access',
    component: Fibit_access
  },
  {
    path: '/Manage_data',
    name: 'Manage_data',
    component: Manage_data
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
