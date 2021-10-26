<template>
  <div class="namecard">
<p class="name2">{{this.$store.state.card_name}}</p>
        <span class="phonetic2">{{this.$store.state.card_furigana}}</span>

        <div class="contact">
            <span><i class="fas fa-school"></i>~~~~~大学</span>
            <span><i class="fas fa-envelope"></i><a href="mailto:---&#64;ac.jp">~~~~~@.ac.jp</a></span>
            <span><i class="fas fa-heart"></i>{{this.$store.state.card_favourite}}</span>
            <span><i class="fab fa-github-square"></i>{{this.$store.state.card_skills}}</span>
        </div>

        <img src="../images/anonymous.jpg" alt="顔画像" style="bottom: 13.0rem">
        <div class="namecard-img">
            <img src="../images/gif-img.gif" alt="gif画像">
        </div>
    </div>
</template>

<script>
export default {
  name: 'card1',
  head: {
    link: [
      { rel: 'stylesheet', href: 'https://use.fontawesome.com/releases/v5.6.3/css/all.css' }
    ]
  },
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    console.log('start')
  },
  methods: {
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
