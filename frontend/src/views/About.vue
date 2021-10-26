<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'home',
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    console.log('start')
    this.updataTableData()
  },
  methods: {
    updataTableData: function () {
      axios.get('http://127.0.0.1:5000/api/spam').then(response => {
        console.log('a')
        console.log(response.data)
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
