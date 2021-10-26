<template>
    <div class="create-page body-content">
        <div class="left-block">
        card area
        <h3>{{this.CARD_NAME}}</h3>
        <h3>{{this.CARD_EMAIL}}</h3>
        <h3>{{this.CARD_MESSAGE}}</h3>
        </div>
        <div class="right-block">
            <form  name="create_form" id="contact-form" class="form-horizontal" role="form">
            <div class="form-group ">
                <div class="col-sm-12">
                <input type="text" class="form-control form-category" id="name" placeholder="NAME" name="name" v-model="FORM_NAME">
                </div>
            </div>

            <div class="form-group">
                <div class="col-sm-12">
                    <input type="email" class="form-control form-category" id="email" placeholder="EMAIL" name="email" v-model="FORM_EMAIL" required>
                </div>
            </div>

                <textarea class="form-control user-detail" v-model="FORM_MESSAGE" rows="10" placeholder="MESSAGE" name="message" required style='font-family: "Yu Gothic medium", "游ゴシック Medium", Yugothic, "游ゴシック体", "ヒラギノ角 Pro W3", sans-serif;'></textarea>
                <a class="button registor" @click="Create" >登録</a>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Create',
  data () {
    return {
      CARD_NAME: '',
      CARD_EMAIL: '',
      CARD_MESSAGE: '',
      FORM_NAME: '',
      FORM_EMAIL: '',
      FORM_MESSAGE: '',
      myresponse: ''
    }
  },
  methods: {
    Create: function () {
      var detail = [{ name: this.FORM_NAME, email: this.FORM_EMAIL, message: this.FORM_MESSAGE }]
      axios.post('http://127.0.0.1:5000/api/spam', detail).then(response => {
        this.$store.dispatch('createCard', { card_name: response.data[0].name, card_email: response.data[0].email, card_message: response.data[0].message })
        console.log(this.$store.state)
        this.CARD_NAME = response.data[0].name
        this.CARD_EMAIL = response.data[0].email
        this.CARD_MESSAGE = response.data[0].message
        this.FORM_NAME = ''
        this.FORM_EMAIL = ''
        this.FORM_MESSAGE = ''
        console.log(response.data)
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.CARD_NAME = this.$store.state.card_name
    this.CARD_EMAIL = this.$store.state.card_email
    this.CARD_MESSAGE = this.$store.state.card_message
  }
}
</script>

<style>
.registor{
    position:absolute;
    left:210px
}
.create-page{
    margin-top:66px;
    display: flex;
}
.right-block{
  text-align:center;
  width:40%;
}
.left-block{
  width:60%;
}
.form-horizontal {
  /*float: left;*/
  width: 400px;
  position:relative;
}
.user-detail{
    height:200px;
}
.form-category{
  height:40px;
  margin-bottom:10px;
}
.form-control,
textarea {
  padding-left:7px;
  font-size:20px;
  resize:none;
  width: 500px;
  background-color: #fff;
  color: #312F2F;
  letter-spacing: 1px;
  border-radius:10px;
  border-width:5px;
  outline :none
}
.user-detail{
  padding-top:10px;
}
.send-button {
  margin-top: 15px;
  height: 34px;
  width: 400px;
  overflow: hidden;
  transition: all .2s ease-in-out;
}

.alt-send-button {
  width: 400px;
  height: 34px;
  transition: all .2s ease-in-out;
}

.send-text {
  display: block;
  margin-top: 10px;
  font: 700 12px 'Lato', sans-serif;
  letter-spacing: 2px;
}

.alt-send-button:hover {
  transform: translate3d(0px, -29px, 0px);
}
</style>
