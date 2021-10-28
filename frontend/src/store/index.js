import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    card_name: '',
    card_furigana: '',
    card_birthday: '',
    card_favourite: '',
    card_skills: '',
    card_code: '',
    show_card: '',
    uID: ''
  },
  mutations: {
    createCard (state, form) {
      state.card_name = form.card_name
      state.card_furigana = form.card_furigana
      state.card_birthday = form.card_birthday
      state.card_favourite = form.card_favourite
      state.card_skills = form.card_skills
      state.card_code = form.card_code
      state.uID = form.uID
    },
    authuID (state, uID) {
      state.uID = uID
    },
    create_code (state, Cardcode) {
      state.card_code = Cardcode.Cardcode
    },
    show_card (state, showCard) {
      state.show_card = showCard.showCard
    }
  },
  actions: {
    createCard (context, form) {
      context.commit('createCard', form)
    },
    authuID (context, uID) {
      context.commit('authuID', uID)
    },
    create_code (context, Cardcode) {
      context.commit('create_code', Cardcode)
    },
    show_card (context, showCard) {
      context.commit('show_card', showCard)
    }
  },
  modules: {
  }
})
