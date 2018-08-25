<template>
  <el-header>
    <div class="input-form">
        <el-row>
          <el-input placeholder="Paste your private key here" prefix-icon="el-icon-edit" v-model="privatekey"></el-input>
          <el-button type="success" icon="el-icon-check" circle v-on:click="submit_privatekey"></el-button>
        </el-row>
    </div>
    <balance-table></balance-table>
  </el-header>
</template>

<style scoped>
  .el-row {
    display: inline-block;
    width: 500px;
    top: 10px;
  }
  .el-col {
    width: 500px;
  }
  .el-input {
    width: 400px;
  }
  .input-form {
    width: 1000px;
    margin: auto;
  }
</style>

<script>
  import { mapState, mapGetters, mapActions } from 'vuex';
  import Balance from '@/components/Balance';
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
      loggedIn(after, before) {
        if(after === true) {
          this.$router.push({ path: `/comics` })
        }
      }
    },
    components: {
        'balance-table': Balance
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
        privatekey: "",
      }
    }
  }
</script>
