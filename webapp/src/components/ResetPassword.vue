<template>
  <div class="sign-up">
    <h3>Enter your Email address and we'll send you a password reset link!</h3>
    <el-form :model="reset" ref="reset">
      <el-row type="flex" justify="center">
        <el-col class="email">
          <el-form-item
            prop="email"
            :rules="[
              { required: true, message: 'Please input email address', trigger: 'blur' },
              { type: 'email', message: 'Please input correct email address', trigger: 'blur' }
            ]"
          >
          <el-input type="email" placeholder="Email" v-model="reset.email"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
      <el-button :loading="reset.disabled" type="primary" @click="submitForm('reset')">Submit</el-button>
      </el-form-item>
    </el-form>
    <p>or go back to <router-link to="login">login</router-link>.</p>
  </div>
</template>

<script>
  import firebase from 'firebase'
  export default {
    data () {
      return {
        reset: {
          email: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.reset.disabled = true
            firebase.auth().sendPasswordResetEmail(this.reset.email).then(
              () => {
                this.reset.disabled = false
                this.$message({
                  showClose: true,
                  message: `Reset Email sent to ${this.reset.email}.`,
                  type: 'success',
                  duration: 15000
                })
                this.$refs['reset'].resetFields()
                this.$router.replace({name: 'Login'})
              },
              (err) => {
                this.reset.disabled = false
                this.$message({
                  showClose: true,
                  message: err.message,
                  type: 'error',
                  duration: 15000
                })
              }
            )
          }
        })
      }
    }
  }
</script>

<style scoped>
  .reset {
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
