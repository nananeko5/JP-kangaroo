import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import firebase from 'firebase/compat/app'
Vue.config.productionTip = false
const config = {
  apiKey: 'AIzaSyACmNZ8E20WFdDCzrw4jXJPTmRbmQ_xuSA',
  authDomain: 'isdl-kangaroo.firebaseapp.com',
  projectId: 'isdl-kangaroo',
  storageBucket: 'isdl-kangaroo.appspot.com',
  messagingSenderId: '639740489459',
  appId: '1:639740489459:web:bd4c94def6c2feedb7d186'
}
firebase.initializeApp(config)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
