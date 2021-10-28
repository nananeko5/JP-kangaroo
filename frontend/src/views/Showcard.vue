<template>
  <div class="namecard">
        <p class="name2">{{this.name}}</p>
        <span class="phonetic2">{{this.furigana}}</span>

        <div class="contact">
            <span><i class="fas fa-school"></i>~~~~~大学</span>
            <span><i class="fas fa-envelope"></i><a href="mailto:---&#64;ac.jp">~~~~~@.ac.jp</a></span>
            <span><i class="fas fa-heart"></i>{{this.favourite}}</span>
            <span><i class="fab fa-github-square"></i>{{this.skills}}</span>
        </div>

        <img src="../images/anonymous.jpg" alt="顔画像" style="bottom: 13.0rem">
        <div class="namecard-img">
            <img src="../images/gif-img.gif" alt="gif画像">
        </div>
        <a class="button" @click='back'>戻る</a>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Showcard',
  head: {
    link: [
      { rel: 'stylesheet', href: 'https://use.fontawesome.com/releases/v5.6.3/css/all.css' }
    ]
  },
  data () {
    return {
      name: '',
      furigana: '',
      birthday: '',
      favourite: '',
      skills: ''
    }
  },
  mounted () {
    console.log('start')
  },
  methods: {
    back: function () {
      this.$router.push('/gallery')
    }
  },
  created () {
    var detail = [{
      uID: this.$store.state.show_card
    }]
    console.log(this.ID)
    axios.post('http://127.0.0.1:5000/api/show_card', detail).then(response => {
      console.log(response.data)
      this.name = response.data.name
      this.furigana = response.data.furigana
      this.birthday = response.data.birthday
      this.favourite = response.data.favourite
      this.skills = response.data.skills
    }).catch(err => {
      alert('カードの作成を行ってください')
      console.log(err)
    })
  }
}
</script>
<style>
.namecard {
            text-align:left;
            background-image:url("../images/background2.png");
            background-size: cover;
            background-repeat: no-repeat
}
</style>
