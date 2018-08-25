<template>
  <div>
    <el-header>
      <balance-table></balance-table>
    </el-header>
    <el-row>

  <!-- <div>
    <ul>
      <li v-for="image in uploadedImages" :key="image">
        <img v-show="image" :src="image.imageHashes[0]" />
      </li>
    </ul>
  </div> -->
  {{ comics }}
      <!-- <el-col :span="4" v-for="(o) in 16" :key="o">
        <el-card :body-style="{ padding: '0px' }">
          <img src="@/assets/jojo.jpeg" class="image">
          <div style="padding: 14px;">
            <span>JoJo</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col> -->
    </el-row>
  </div>
</template>

<style>
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .el-row {
    top: 10px;
  }

  .el-col {
    margin: 15px;
  }
</style>

<script>
  import { mapState, mapGetters, mapActions } from 'vuex';
  import Balance from '@/components/Balance';

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
    name: 'privatekey-input',
    computed: {
      ...mapState([
        'address',
        'balance',
        'loggedIn',
      ]),
    },
    watch: {
    },
    components: {
        'balance-table': Balance
    },
    created: async function() {
      let comics = await getComics()
      this.comics = comics
      console.log(this.comics)
    },
    methods: {
      ...mapActions([
          'SUBMIT_PRIVATEKEY',
      ]),
      submit_privatekey() {
          this.SUBMIT_PRIVATEKEY(this.privatekey)
          this.privatekey = ""
      }
    },
    data() {
      return {
        comics: [],
        privatekey: "",
        currentDate: new Date()
      }
    }
  }
</script>
