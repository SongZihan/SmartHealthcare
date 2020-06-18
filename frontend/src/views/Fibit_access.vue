<template>
    <div>
      <p>please wait</p>
      {{this.$route.hash}}
    </div>
</template>

<script>
export default {
  name: 'Fibit_access',
  mounted () {
    // 页面加载完成后自动执行post请求传递token给服务器
    this.post_data()
  },
  methods: {
    post_data () {
      this.$axios({
        method: 'get',
        url: '/api/get_fibit_token',
        params: {
          token: this.$route.hash
        },
        // 手动添加jwt请求头
        headers: {
          Authorization: localStorage.token
        }
      }).then((res) => {
        if (res.data.code === 200) {
          // 添加token到本地
          localStorage.fibit_token = 'Bearer ' + res.data.data
          this.$router.push({ name: 'Manage_data' })
        }
      })
    }
  }

}
</script>

<style scoped>

</style>
