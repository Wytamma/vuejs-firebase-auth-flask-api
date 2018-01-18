<template>
  <div class="sign-up">
    <h3>Enter your Email address and we'll send you a sign up link!</h3>
    <el-form :model="signUp" ref="signUp">
      <el-row type="flex" justify="center">
        <el-col class="email">
          <el-form-item
            prop="email"
            :rules="[
              { required: true, message: 'Please input email address', trigger: 'blur' },
              { type: 'email', message: 'Please input correct email address', trigger: 'blur' }
            ]"
          >
          <el-input type="email" placeholder="Email" v-model="signUp.email"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
      <el-button :loading="signUp.disabled" type="primary" @click="submitForm('signUp')">Sign up</el-button>
      </el-form-item>
    </el-form>
    <p>or go back to <router-link to="login">login</router-link>.</p>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        signUp: {
          email: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // GET /someUrl
            this.signUp.disabled = true
            this.$http.get(process.env.API_URL + '/auth/signup/' + this.signUp.email).then(response => {
              this.$message({
                showClose: true,
                message: `Sign up Email sent to ${this.signUp.email}.`,
                type: 'success',
                duration: 15000
              })
              this.$refs['signUp'].resetFields()
              this.signUp.disabled = false
              // success callback
            }, response => {
              // error callback
              this.signUp.disabled = false
              this.$message({
                showClose: true,
                message: response.body.message,
                type: 'error',
                duration: 15000
              })
            })
          }
        })
      }
    }
  }
</script>

<style scoped>
  .signUp {
    margin-top: 40px;
  }
  .email {
    max-width: 300px;
    margin: 10px;
  }
  span {
    display: block;
    margin-top: 20px;
    font-size: 11px;
  }
  p {
    margin-top: 40px;
    font-size: 13px;
  }
  p a {
    text-decoration: underline;
    cursor: pointer;
  }
</style>
