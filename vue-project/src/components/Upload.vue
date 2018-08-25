<template>
  <div>
    <ul>
      <li v-for="image in uploadedImages" :key="image">
        <img v-show="image" :src="image.imageHashes[0]" />
      </li>
    </ul>
  </div>
</template>

<style>
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
        currentDate: new Date()
      }
    }
  }
</script>
