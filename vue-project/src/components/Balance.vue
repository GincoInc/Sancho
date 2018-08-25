<template>
  <div class="balance-table">
    <span>NEO: {{ this.balance.NEO }}</span>
    <span>GAS: {{ this.balance.GAS }}</span>
    <span>LoginToken: {{ this.balance.LoginToken }}</span>
    <span>Address: {{ this.address }}</span>
  </div>
</template>

<style>
  .balance-table {
    text-align: right;
  }
</style>

<script>
  import { mapState, mapGetters, mapActions } from 'vuex';
  export default {
    name: 'balance-table',
    computed: {
      ...mapState([
        'address',
        'balance',
      ]),
    },
    data() {
      return {
        tableData: [{
            currency: 'NEO',
            balance: '0',
          }, {
            currency: 'GAS',
            balance: '0',
        }]
      }
    }
  }
</script>
