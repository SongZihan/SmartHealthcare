<template>
  <el-container>
    <el-header>
      <el-row>
        <el-col :span="6" :offset="18">
          <el-button type="danger" round @click="logout">logout</el-button>
        </el-col>
      </el-row>

    </el-header>
  <el-container>
    <el-aside width="300px">
      <el-row>
        <el-col>
          <el-button @click="Daily_activity">Get Daily Activity Summary</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-button type="primary" @click="sleep_summary">Sleep Summary</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-button type="success">etc</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-button type="info">etc</el-button>
        </el-col>
      </el-row>
    </el-aside>
    <el-main>
      <el-row>
        <el-col>
          <div class="block">
            <el-date-picker
              v-model="value1"
              type="date"
              placeholder="select date">
            </el-date-picker>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-collapse v-model="activeNames">
            <el-collapse-item :title="index" :name="index" v-for="(i,index) in this.res_data" :key="index">
              <div>{{i}}</div>
            </el-collapse-item>
          </el-collapse>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
  </el-container>

</template>

<script>
export default {
  name: 'Manage_data',
  data () {
    return {
      value1: '',
      res_data: '',
      activeNames: []
    }
  },
  computed: {
    date_data () {
      // 返回日期格式 xxxx-xx-xx
      var date = new Date(this.value1)
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
    }
  },
  methods: {
    Daily_activity () {
      this.$axios({
        method: 'get',
        url: 'https://api.fitbit.com/1/user/-/activities/date/' + this.date_data + '.json',
        headers: {
          Authorization: localStorage.fibit_token
        }
      }).then((res) => {
        this.res_data = res.data
      })
    },
    sleep_summary () {
      this.$axios({
        method: 'get',
        url: 'https://api.fitbit.com/1.2/user/-/sleep/date/' + this.date_data + '.json',
        headers: {
          Authorization: localStorage.fibit_token
        }
      }).then((res) => {
        this.res_data = res.data
      })
    },
    logout () {
      // 返回主页,删除token
      this.$store.commit('del_token')
      // 清除所有cookie
      var keys = document.cookie.match(/[^ =;]+(?=)/g)
      if (keys) {
        for (var i = keys.length; i--;) { document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString() }
      }
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
  .el-row {
    margin: 5ex;
  }
</style>
