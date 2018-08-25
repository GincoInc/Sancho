<template>
  <div id="comic">
    <ul>
      <li v-for="(comic, index) in $store.state.comics" :key="index">
        <img v-show="comic" :src="'https://ipfs.io/ipfs/'+ comic.imageHashes[0]" />
      </li>
    </ul>
  </div>
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
    this.$store.state.comics = await getComics()
  },
  data() {
    return {
    }
  },
  methods :{
  }
};

</script>