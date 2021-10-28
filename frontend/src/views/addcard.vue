<template>
    <div id="app" class="container">
        <input type='text' class='form-control form-category' id='name' placeholder='NAME' name='name' v-model='card_code'>
        <a class='button registor' @click='addcard' >追加</a>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'addcard',
  data () {
    return {
      card_code: '',
      uID: ''
    }
  },
  mounted () {
  },
  methods: {
    addcard: function () {
      var detail = [{
        card_code: this.card_code,
        uID: this.uID
      }]
      console.log(this.uID)
      axios.post('http://127.0.0.1:5000/api/add_gallery', detail).then(response => {
        alert(response.data.addname)
      }).catch(err => {
        alert('名刺が見つかりませんでした')
        console.log(err)
      })
    }
  },
  created () {
    this.uID = this.$store.state.uID
  }
}
</script>
