<template>
  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="ID" prop="username">
        <el-input v-model="ruleForm.username" autocomplete="on"></el-input>
      </el-form-item>
      <el-form-item label="invite code">
        <el-input v-model="ruleForm.register_key" autocomplete="on"></el-input>
      </el-form-item>
      <el-form-item label="password" type="password" prop="password">
        <el-input v-model.number="ruleForm.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">submit</el-button>
        <el-button @click="resetForm('ruleForm')">reset</el-button>
        <el-button @click="to_main">Home</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Registered',
  data () {
    // 添加了一些辅助验证，可以在提交前对表单格式进行验证
    var checkID = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('ID不能为空'))
      } else {
        callback()
      }
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }

    return {
      ruleForm: {
        username: '',
        password: '',
        register_key: ''
      },
      centerDialogVisible: false,
      rules: {
        password: [
          { validator: validatePass, trigger: 'blur' }
        ],
        username: [
          { validator: checkID, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    to_registered: function () {
      this.$router.push('Registered')
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    to_main () {
      this.$router.push('/')
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 转换为字符串
          this.ruleForm.password += ''
          this.ruleForm.username += ''
          this.ruleForm.register_key += ''
          // 发起post请求
          this.$axios({
            method: 'post',
            url: '/api/register',
            data: this.ruleForm
          }).then((res) => {
            if (res.data.code === 200) {
            // 注册完成去往获取设备数据页面
            //   window.location.href = process.env.VUE_APP_fibit_url
            //   window.open()
              // 返回登录页面
              this.$router.push('/')
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>
