

<template>
  <div id="login">
    <div class="wrapper_form_header">
      <input class="input_key_header" type="" name="" placeholder="ここに秘密鍵を入力してください" v-model="privateKey">
      <button class="button_go_header" v-on:click="login">GO</button>
      <button class="button_upload_header">Upload</button>
    </div>
  </div>
</template>

<script>
import Neon, {api, rpc, wallet, u} from '@cityofzion/neon-js'

export default {
  data() {
    return {
      privateKey: "",
      isLogin: false
    }
  },
  methods :{
    login: function () {
      const account = new wallet.Account(this.privateKey);
      this.$store.commit('login', account.privateKey)
      this.$router.push('/comics')
    }
  },
};

</script>