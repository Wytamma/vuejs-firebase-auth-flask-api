<template>
  <div class="login">
    <h3>Sign In</h3>
    <el-form :model="signIn" ref="signIn">
      <el-row type="flex" justify="center">
        <el-col class="input">
          <el-input type="email" placeholder="Email" v-model="signIn.email"></el-input>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col class="input">
          <el-input type="password" placeholder="Password" v-model="signIn.password"></el-input><br>
        </el-col>
      </el-row>
      <el-button type="primary" :loading="signIn.disabled" @click="submitForm('signIn')">Sign In</el-button>
    </el-form>
    <p>You don't have an account ? You can <router-link :to="{name: 'SignUp'}">create one</router-link></p>
    <p>Forgot your password? Click this <router-link :to="{name: 'ResetPassword'}">link</router-link></p>

  </div>
</template>

<script>
  import firebase from 'firebase'

  export default {
    name: 'login',
    data: function () {
      return {
        signIn: {
          email: '',
          password: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.signIn.disabled = true
        firebase.auth().signInWithEmailAndPassword(this.signIn.email, this.signIn.password).then(
          (user) => {
            this.signIn.disabled = false
            this.$message.closeAll()
            this.$router.replace({name: 'Hello'})
          },
          (err) => {
            this.signIn.disabled = false
            this.$message({
              showClose: true,
              message: err.message,
              type: 'error',
              duration: 15000
            })
          }
        )
      }
    }
  }
</script>

<style scoped>  /* "scoped" attribute limit the CSS to this component only */
  .login {
    margin-top: 40px;
  }
  input {
    margin: 10px 0;
    width: 20%;
    padding: 15px;
  }
  .input {
    max-width: 300px;
    margin: 10px;
  }
  button {
    margin-top: 10px;
    margin-bottom: 20px;
  }
  p {
    font-size: 13px;
  }
  p a {
    text-decoration: underline;
    cursor: pointer;
  }
  .el-icon-close {
    padding: 10px;
    margin: 10px;
  }
</style>
