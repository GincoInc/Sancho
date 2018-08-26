import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    scriptHash: '619d317cd320f8b447a662d91628e341d0e0507d',
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
