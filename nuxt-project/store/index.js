import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    privateKey: '',
    isLogin: false,
    comics: []
  },
  mutations: {
    login (state, privateKey) {
      state.privateKey = privateKey
      state.isLogin = true
    },
    setComics(state, comics) {
      state.comics = comics
    }
  }
})

export default store