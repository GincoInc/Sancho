import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    scriptHash: '4c4a20c3979430d6176eeea9bfd2b4e5dd675c71',
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
