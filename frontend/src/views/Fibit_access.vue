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
      })
    }
  }

}
</script>

<style scoped>

</style>
