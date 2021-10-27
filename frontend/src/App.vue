<template>
  <div id="app">
    <header class="page-header wrapper" >
      <h1><a href="index.html"><img class="logo" src="./images/logo.svg" alt="NameCaホーム"/></a></h1>
      <nav>
        <ul class="main-nav">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/create">Create</router-link></li>
          <li><router-link to="/signin">Sign In</router-link></li>
          <li @click='logout'>Log Out</li>
        </ul>
      </nav>
    </header>
    <router-view />

    <footer>
      <div class="wrapper">
        <p><small>&copy; 2021 JP-Kangaroo</small></p>
      </div>
    </footer>
  </div>
</template>

<script>
import firebase from 'firebase/compat/app'
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name
    }
  },
  methods: {
    logout: function () {
      firebase.auth().signOut().then(() => {
        this.$router.push('/')
        this.$store.dispatch('createCard', { card_name: '', card_furigana: '', card_birthday: '', card_favourite: '', card_skills: '', uID: '' })
      })
    }
  }
}
</script>

<style scoped>
#app {
   font-family: "Yu Gothic medium", "游ゴシック Medium", Yugothic, "游ゴシック体", "ヒラギノ角 Pro W3", sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
.body-content{
  height:380px;
}
</style>

<style lang="scss">
@import './css/style.css';

</style>
