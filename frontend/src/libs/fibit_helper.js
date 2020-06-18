import axios from 'axios'
// 创建一个axios实例

function check_token (self, token) {
  // 接收token，返回token验证的结果，成功则去manage_data页面，失败则去fibit授权页面
  axios({
    method: 'get',
    url: 'https://api.fitbit.com/1/user/-/profile.json',
    headers: {
      Authorization: 'Bearer ' + token
    }
  }).then((res) => {
    // console.log('请求成功')
    self.$notify({
      title: '成功',
      message: 'successfully get auth',
      type: 'success'
    })
    // 将token数据存入localSession
    localStorage.fibit_token = 'Bearer ' + token
    // 去数据管理页面
    self.$router.push('Manage_data')
  }).catch((err) => {
    // console.log('请求失败')
    self.$notify.error({
      title: '错误',
      message: err
    })
    // 去授权页面
    window.location.href = process.env.VUE_APP_fibit_url
    window.open()
  })
}

export {
  check_token
}
