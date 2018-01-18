import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'
import SetPassword from '@/components/SetPassword'
import ResetPassword from '@/components/ResetPassword'
import Auth from '@/components/Auth'
import firebase from 'firebase'

Vue.use(Router)

let router = new Router({
  mode: 'history', /* may have to change back to /#/ mode */
  routes: [
    {
      path: '*',
      redirect: '/auth/login'
    },
    {
      path: '/',
      redirect: '/auth/login'
    },
    {
      path: '/auth',
      redirect: '/auth/login',
      component: Auth,
      children: [
        {
          path: 'login',
          name: 'Login',
          component: Login
        },
        {
          path: 'sign-up',
          name: 'SignUp',
          component: SignUp
        },
        {
          path: 'set-password',
          name: 'SetPassword',
          component: SetPassword
        },
        {
          path: 'reset-password',
          name: 'ResetPassword',
          component: ResetPassword
        }
      ]
    },
    {
      path: '/hello',
      name: 'Hello',
      component: HelloWorld,
      meta: {
        requiresAuth: true
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  let currentUser = firebase.auth().currentUser
  let requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth && !currentUser) next('login')
  else if (!requiresAuth && currentUser) next('hello')
  else next()
})

export default router
