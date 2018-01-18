<template>
  <div class="auth">
    <img src="../assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'auth'
}
</script>

<style scoped>
 .auth {
   margin-top: 40px;
 }
</style>
