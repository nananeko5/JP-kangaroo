<template>
    <div id="app" class="container">
        <h1>Gallery</h1>
        <ul>
            <li v-for="(person, index) in people" :key="index">
                <button v-on:click="showCard(index)">
                    {{ person.name }}
                </button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'gallery',
  data () {
    return {
      people: [],
      uID: ''
    }
  },
  mounted () {
    console.log('start')
  },
  methods: {
    showCard: function (index) {
      var cardID
      cardID = this.people[index].id
      this.$store.dispatch('show_card', { showCard: cardID })
      this.$router.push('/showcard')
    }
  },
  created () {
    this.uID = this.$store.state.uID
    console.log(this.uID)
    var detail = [{
      uID: this.$store.state.uID
    }]
    axios.post('http://127.0.0.1:5000/api/show_gallery', detail).then(response => {
      console.log(response.data)
      var data = {
        id: '',
        name: '',
        imgpath: ''
      }
      for (var i in response.data) {
        data = {
          id: response.data[i].id,
          name: response.data[i].name,
          imgpath: response.data[i].imgpath
        }
        this.people.push(data)
      }
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>
