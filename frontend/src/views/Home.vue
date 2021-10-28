<template>
  <div class="home-content wrapper body-content">

    <modal name="card_code" :draggable="true" :resizable="true">
        <div class="modal-header">
          <h2>名刺交換コード</h2>
        </div>
        <div class="modal-body">
        <div class="changename" style="float:left">
          <p class="change_p">コード：</p>
          <b-form-input v-model="card_code" ></b-form-input>
        </div>
        <div class="footbtn">
          <b-button variant="primary" class="chengebtn" v-on:click="cardcode_update">更新</b-button>
          <b-button variant="secondary" v-on:click="hide" class="chengebtn">閉じる</b-button>
        </div>
        </div>
    </modal>

    <button class="optionbtn"  v-on:click="show" >
      名刺コード
    </button>
    <h2 class="page-title">NameCa</h2>
    <p >カジュアルな名刺交換を体験してみませんか</p>
    <a class="button" @click='Toaddcard'>Add Card</a>
    <a class="button2" @click='ToGallery'>Gallery</a>
  </div><!-- /.home-content -->
</template>

<script>
import axios from 'axios'
export default {
  name: 'home',
  data () {
    return {
      card_code: '',
      uID: ''
    }
  },
  methods: {
    show: function () {
      this.$modal.show('card_code')
    },
    hide: function () {
      this.$modal.hide('card_code')
    },
    cardcode_update: function () {
      var detail = [{
        card_code: this.card_code,
        uID: this.uID
      }]
      axios.post('http://127.0.0.1:5000/api/card_code', detail).then(response => {
        console.log(response.data.card_code)
        if (response.data.flag === 1) {
          alert('このコードは既に使用されています')
        } else {
          this.$store.dispatch('create_code', { Cardcode: response.data.card_code })
          this.card_code = this.$store.state.card_code
          this.hide()
        }
      }).catch(err => {
        alert('カードの作成を行ってください')
        console.log(err)
      })
    },
    Toaddcard: function () {
      this.$router.push('/addcard')
    },
    ToGallery: function () {
      this.$router.push('/gallery')
    }
  },
  created () {
    this.card_code = this.$store.state.card_code
    this.uID = this.$store.state.uID
    console.log(this.uID)
  }

}
</script>
