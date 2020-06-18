import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data: [],
    is_login: false,
    token: ''
  },
  mutations: {

    set_token (state, token) {
      // 顺便修改登录状态
      state.is_login = true
      state.token = token
      localStorage.token = token
    },
    del_token (state) {
      // 顺便修改登录状态
      state.is_login = false
      state.token = ''
      localStorage.removeItem('token')
      localStorage.removeItem('fibit_token')
    }
  },
  actions: {
  },
  modules: {
  }

})
