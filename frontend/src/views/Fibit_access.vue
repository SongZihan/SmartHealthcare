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
    // 传递token
    this.post_data()
  },
  methods: {
    post_data () {
      this.$axios({
        method: 'get',
        url: '/api/get_fibit_token',
        params: {
          token: this.$route.hash
        }
      }).then((res) => {
        if (res.data.code === -1) {
          this.$notify.error({
            title: '错误',
            message: res.data.msg + '||' + res.data.data
          })
          console.log('i get the error')
        } else if (res.data.code === 200) {
          this.$notify({
            title: '成功',
            message: res.data.msg,
            type: 'success'
          })
        }
      })
    }
  }

}
</script>

<style scoped>

</style>
