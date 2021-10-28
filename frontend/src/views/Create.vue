<template>
    <div class='create-page body-content'>
        <div class='left-block'>
        <Card1 />
        </div>
        <div class='right-block'>
            <form  name='create_form' id='contact-form' class='form-horizontal' role='form'>
            <div class='form-group '>
                <div class='col-sm-12'>
                <input type='text' class='form-control form-category' id='name' placeholder='NAME' name='name' v-model='FORM_NAME'>
                </div>
            </div>

            <div class='form-group'>
                <div class='col-sm-12'>
                    <input type='text' class='form-control form-category' id='furigana' placeholder='FURIGANA' name='furigana' v-model='FORM_FURIGANA' required>
                </div>
            </div>
            <div class='form-group'>
                <div class='col-sm-12'>
                    <input type='date' class='form-control form-category' id='birthday' placeholder='BIRTHDAY' name='birthday' v-model='FORM_BIRTHDAY' required>
                </div>
            </div>
            <div class='form-group'>
                <div class='col-sm-12'>
                    <input type='text' class='form-control form-category' id='favourite' placeholder='FAVOURITE' name='favourite' v-model='FORM_FAVOURITE' required>
                </div>
            </div>
            <div class='form-group'>
                <div class='col-sm-12'>
                    <input type='text' class='form-control form-category' id='skills' placeholder='SKILLS' name='skills' v-model='FORM_SKILLS' required>
                </div>
            </div>
               <!-- <textarea class='form-control user-detail' v-model='FORM_FAVOURITE' rows='10' placeholder='FAVOURITE' name='favourite' required style='font-family: 'Yu Gothic medium', '游ゴシック Medium', Yugothic, '游ゴシック体', 'ヒラギノ角 Pro W3', sans-serif;'></textarea>-->
                <a class='button registor' @click='Create' >登録</a>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Card1 from './card1'

export default {
  components: { Card1 },
  name: 'Create',
  data () {
    return {
      CARD_NAME: '',
      CARD_FURIGANA: '',
      CARD_BIRTHDAY: '',
      CARD_FAVOURITE: '',
      CARD_SKILLS: '',
      FORM_NAME: '',
      FORM_FURIGANA: '',
      FORM_BIRTHDAY: '',
      FORM_FAVOURITE: '',
      FORM_SKILLS: '',
      myresponse: ''
    }
  },
  methods: {
    Create: function () {
      console.log(this.FORM_BIRTHDAY)
      var detail = [{
        img: '../images/hakase.jpg',
        name: this.FORM_NAME,
        furigana: this.FORM_FURIGANA,
        birthday: this.FORM_BIRTHDAY,
        favourite: this.FORM_FAVOURITE,
        skills: this.FORM_SKILLS,
        card_code: this.$store.state.card_code,
        uID: this.$store.state.uID
      }]
      console.log(detail)
      axios.post('http://127.0.0.1:5000/api/design', detail).then(response => {
        console.log(response.data)
        console.log(response.data.name)
        console.log(response.data.furigana)
        this.$store.dispatch('createCard', {
          card_name: response.data.name,
          card_furigana: response.data.furigana,
          card_birthday: response.data.birthday,
          card_favourite: response.data.favourite,
          card_skills: response.data.skills,
          uID: this.$store.state.uID
        })
        console.log(this.$store.state)
        this.CARD_NAME = response.data.name
        this.CARD_FURIGANA = response.data.furigana
        this.CARD_BIRTHDAY = response.data.birthday
        this.CARD_FAVOURITE = response.data.favourite
        this.CARD_SKILLS = response.data.skills
        this.FORM_NAME = ''
        this.FORM_FURIGANA = ''
        this.FORM_BIRTHDAY = ''
        this.FORM_FAVOURITE = ''
        this.FORM_SKILLS = ''
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.CARD_NAME = this.$store.state.card_name
    this.CARD_FURIGANA = this.$store.state.card_furigana
    this.CARD_BIRTHDAY = this.$store.state.card_birthday
    this.CARD_FAVOURITE = this.$store.state.card_favourite
    this.CARD_SKILLS = this.$store.state.card_skills
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
