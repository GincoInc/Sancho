<template>
  <div>
    <el-header>
      <balance-table></balance-table>
    </el-header>
    <el-row>
      <el-col :span="4" v-for="(o, index) in 16" :key="o">
        <el-card :body-style="{ padding: '0px' }">
          <img src="@/assets/jojo.jpeg" class="image">
          <div style="padding: 14px;">
            <span>JoJo</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
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
