<template>
  <section id="archives">
    <ul class="wrapper_contents_archives">
      <li class="each_book_archives" v-for="(comic, index) in $store.state.comics" :key="index">
        <article class="thumbnail_archives">
          <div v-on:click="goDetail(comic.hash)">
            <img :src="'https://ipfs.io/ipfs/'+ comic.imageHashes[0]">
          </div>
        </article>
      </li>
    </ul>
  </section>
</template>

<script>
import Neon, {api, rpc, wallet, u} from '@cityofzion/neon-js'

async function getComics() {
  const props = {
    scriptHash: '8e1ed289c3e66335de89bfb39265057f49828ecd', // Scripthash for the contract
    operation: 'getData', // name of operation to perform.
    args: [] // any optional arguments to pass in. If null, use empty array.
  }
  let script = Neon.create.script(props)
  let res = await rpc.Query.invokeScript(Neon.create.script(props)).execute('http://localhost:30333')
  return JSON.parse('[' + u.hexstring2str(res.result.stack[0].value) + ']')
}

export default {
  components: {},
  beforeCreate: async function() {
    let comics = await getComics()
    this.$store.commit('setComics', comics) 
  },
  data() {
    return {
    }
  },
  methods :{
    goDetail(hash) {
      this.$router.push('/comics/' + hash)
    }
  }
};

</script>