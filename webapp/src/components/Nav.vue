<template>
  <div v-if="$route.path.indexOf('/auth/') !== -1 ? false : true">
    <el-menu mode="horizontal">
      <el-row >
          <el-col :span="12">
              <el-menu-item class="navbar__title">
                <a href="https://github.com/Wytamma/" target="_blank">vuejs-firebase-auth-flask-api</a>
              </el-menu-item>
          </el-col>
          <el-col :span="12">
            <div class="nav_right">
              <el-menu-item  v-on:click="logout">Logout</el-menu-item>
            </div>
          </el-col>
      </el-row>
    </el-menu>
  </div>
</template>
<script>
  import firebase from 'firebase'
  export default {
    data () {
      return {
      }
    },
    methods: {
      logout: function () {
        firebase.auth().signOut().then(() => {
          this.$router.replace('login')
        })
      }
    }
  }
</script>
<style>
    .nav_right {
      float: right;
    }
    .navbar__title {
        margin-top: 0;
        margin-bottom: 0;
        margin-left: 12px;
        height: 60px;
        line-height: 60px;
        font-size: 1em;
        font-weight: bold;
        float: left;
    }
    .navbar__title a {
        color: #48576a;
        text-decoration: none;
    }
</style>
