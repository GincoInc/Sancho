<template>
  <div id="comics">
    <ul>
      <li v-for="(image, index) in uploadedImages" :key="index">
        <img v-show="image" :src="'https://ipfs.io/ipfs/'+ image.imageHashes[0]" />
      </li>
    </ul>
  </div>
</template>

<script>
import Neon, {api, rpc, wallet, u} from '@cityofzion/neon-js'

const account = new wallet.Account('KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr')
const client = new rpc.RPCClient('http://localhost:30333', '2.7.6')
const config = {
  name: 'http://127.0.0.1:30333',
  extra: {
    neoscan: 'http://127.0.0.1:4000/api/main_net'
  }
}
const privateNet = new rpc.Network(config)
Neon.add.network(privateNet)

async function getImages() {
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
  created: async function() {
    this.uploadedImages = await getImages()
  },
  data() {
    return {
      uploadedImages: [],
    }
  },
  methods :{
  }
};

</script>