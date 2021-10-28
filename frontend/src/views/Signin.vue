<template>
  <div class="signin">
    <h2>Sign in</h2>
    <input type="text" placeholder="Username" v-model="username">
    <input type="password" placeholder="Password" v-model="password">
    <button @click="signIn">Signin</button>
    <p>You don't have an account?
      <router-link to="/signup">create account now!!</router-link>
    </p>
  </div>
</template>

<script>
import firebase from 'firebase/compat/app'
import axios from 'axios'
export default {
  name: 'Signin',
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    signIn: function () {
      firebase.auth().signInWithEmailAndPassword(this.username, this.password).then(
        user => {
          var detail = [{
            uID: firebase.auth().currentUser.uid
          }]
          axios.post('http://127.0.0.1:5000/api/user_info', detail).then(response => {
            this.$store.dispatch('createCard', {
              card_name: response.data.name,
              card_furigana: response.data.furigana,
              card_birthday: response.data.birthday,
              card_favourite: response.data.favourite,
              card_skills: response.data.skills,
              card_code: response.data.card_code,
              uID: firebase.auth().currentUser.uid
            })
            console.log(this.$store.state)
            this.$router.push('/')
          }).catch(err => {
            console.log(firebase.auth().currentUser.uid)
            this.$store.dispatch('authuID', { uID: firebase.auth().currentUser.uid })
            console.log(err)
            this.$router.push('/')
          })
        },
        err => {
          alert(err.message)
        }
      )
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.signin {
  margin-top: 20px;

  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center
}
input {
  margin: 10px 0;
  padding: 10px;
}
</style>
