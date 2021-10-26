import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    card_name: '',
    card_email: '',
    card_message: ''
  },
  mutations: {
    createCard (state, form) {
      state.card_name = form.card_name
      state.card_email = form.card_email
      state.card_message = form.card_message
    }
  },
  actions: {
    createCard (context, form) {
      context.commit('createCard', form)
    }
  },
  modules: {
  }
})
