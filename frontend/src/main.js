import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import firebase from 'firebase/compat/app'
import VModal from 'vue-js-modal'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VModal)
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
