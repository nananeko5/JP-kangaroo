<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:5000'
export default {
  name: 'home',
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    this.updataTableData()
  },
  methods: {
    updataTableData: function () {
      axios.post('/api/spam').then(response => {
        console.log(response.data)
      }).catch(err => {
        console.log(err)
        return null
      })
    }
  }
}
</script>
