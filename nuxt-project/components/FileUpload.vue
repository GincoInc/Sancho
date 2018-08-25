<template>
  <div id="app">
    <ul>
      <li v-for="image in uploadedImages" :key="image">
        <img v-show="image" :src="'https://ipfs.io/ipfs/'+ image.imageHashes[0]" />
      </li>
    </ul>
    <div class="file">
      <label class="file-label">
        <input class="file-input" type="file" name="resume" v-on:change="onFileChange" multiple>
        <span class="file-cta">
          <span class="file-icon">
            <i class="fas fa-upload"></i>
          </span>
          <span class="file-label">
            Choose a file…
          </span>
        </span>
      </label>
    </div>
  </div>
</template>

<script>
import ipfsAPI from 'ipfs-api'
const ipfs = ipfsAPI('localhost', '5001')
import * as neon from '@cityofzion/neon-js'
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
    onFileChange(e) {
      let uploadedImageHashes = []
      let files = e.target.files || e.dataTransfer.files;
      for (let file of files) {
        let reader = new FileReader();
        reader.onload = (e) => {
          let buf = new Buffer(e.target.result)
          ipfs.files.add(buf, (err, file) => {
            if (err) {
              console.log(err);
            }
            uploadedImageHashes.push(file[0].hash);
            if (files.length == uploadedImageHashes.length) {
              const json = JSON.stringify({ title: "hoge", imageHashes: uploadedImageHashes })
              console.log(json)

              Neon.doInvoke({
                net: "http://127.0.0.1:30333",
                script: Neon.create.script({
                  scriptHash: '8e1ed289c3e66335de89bfb39265057f49828ecd', // Scripthash for the contract
                  operation: 'putData', // name of operation to perform.
                  args: [u.str2hexstring(json)]
                }),
                account: account,
                gas: 1
              }).then(res => {
                console.log(res);
              }).catch(e => {
                console.log(e);
              });
            }
          });
        };
        reader.readAsArrayBuffer(file);
      }
    }
  }
};

</script>