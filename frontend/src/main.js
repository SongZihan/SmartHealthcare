import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.config.productionTip = false

// 全局请求头
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'
// 全局超时时间
axios.defaults.timeout = 10000
// 刷新页面时应该自动去sessionStorage中寻找token
axios.defaults.headers.common.Authorization = sessionStorage.token

Vue.prototype.$axios = axios

var vm = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// 全局响应拦截器
axios.interceptors.response.use(function (response) {
  // Any status code that lie within the range of 2xx cause this function to trigger
  // Do something with response data
  if (response.data.code === -1) {
    vm.$notify.error({
      title: '错误',
      message: response.data.msg + '||' + response.data.data
    })
    console.log('i get the error')
  } else if (response.data.code === 200) {
    vm.$notify({
      title: '成功',
      message: response.data.msg,
      type: 'success'
    })
  }
  return response
})
