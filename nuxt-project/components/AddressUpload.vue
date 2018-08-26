<template>
  <div class="wrapper_form_header">
    <div class="wrapper_balance_header">
      <span class="subtitle_balance_header">Address:</span>
      <span class="balance_header">{{ address }}</span>
      <span class="subtitle_balance_header">NeoGas:</span>
      <span class="balance_header">{{ $store.state.neoGas }}</span>
    </div>
    <button class="button_go_header" v-on:click="goUpload">Upload</button>
  </div>
</template>

<script>
import Neon, {api, rpc, wallet, u} from '@cityofzion/neon-js'

export default {
  components: {},
  created: function() {
    const account = new wallet.Account(this.$store.state.privateKey);
    this.address = account.address;
  },
  data() {
    return {
      address: ""
    }
  },
  methods :{
    goUpload(hash) {
      this.$router.push('/upload')
    }
  }
};

</script>
