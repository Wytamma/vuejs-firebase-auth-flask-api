<template>
  <div class="set-password">
    <h3>Set your password</h3>
    <el-form :model="setpassword" ref="setpassword">
      <el-row type="flex" justify="center">
        <el-col class="password">
          <el-form-item
            prop="password"
            :rules="[
              { required: true, message: 'Please enter a password', trigger: 'blur' },
              { min: 8, max: 32, message: 'Password length should be 8 to 32', trigger: 'blur' }
            ]"
          >
          <el-input type="password" placeholder="Password" v-model="setpassword.password"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
        <el-button :loading="setpassword.disabled" type="primary" @click="submitForm('setpassword')">Submit</el-button>
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
        setpassword: {
          password: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // post data
            this.setpassword.disabled = true
            this.$http.post(process.env.API_URL + '/auth/set_password',
              {
                'token': this.$route.query.token,
                'password': this.setpassword.password
              }).then(response => {
              // success callback
                this.setpassword.disabled = false
                firebase.auth().signInWithCustomToken(response.body.token).then(
                  () => {
                    this.$router.replace({name: 'Hello'})
                  }).catch(
                  (error) => {
                      // Handle Errors here.
                    console.log(error.code)
                    console.log(error.message)
                  })
              }, response => {
              // error callback
                this.setpassword.disabled = false
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
  .set-password {
    margin-top: 40px;
  }
  .password {
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
