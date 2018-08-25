import Vue from 'vue';
import Vuex from 'vuex';
import Neon, { rpc, api, wallet, u } from '@cityofzion/neon-js';
const privateNetURL = 'http://localhost:4000';
const privateNet = new rpc.Network({
    name: 'PrivateNet',
    extra: {
        neoscan: privateNetURL + '/api/main_net',
    }
})
Neon.add.network(privateNet)

Vue.use(Vuex)

const state = {
    privatekey: "",
    address: "",
    balance: {
        NEO: "0",
        GAS: "0",
        LoginToken: "0",
    },
    loggedIn: false,
}

const SUBMIT_PRIVATEKEY = 'SUBMIT_PRIVATEKEY';

const mutations = {
    async SUBMIT_PRIVATEKEY(state, privatekey) {
        if (privatekey !== "") {
            state.privatekey = privatekey;
            const account = new wallet.Account(state.privatekey);
            state.address = account.address;
            const balance = await api.neoscan.getBalance('TestNet', state.address)
            state.balance.NEO = balance.assets.NEO.balance.toString();
            state.balance.GAS = balance.assets.GAS.balance.toString();
            const props = {
                scriptHash: '4dd514ee7b7f739d88d779c9be2671797651dde0', // Scripthash for the contract
                operation: 'balanceOf', // name of operation to perform.
                args: [u.reverseHex(wallet.getScriptHashFromAddress(state.address))] // any optional arguments to pass in. If null, use empty array.
            }
            const script = Neon.create.script(props);
            const response = await rpc.Query.invokeScript(script).execute('http://localhost:30333');
            const tokenBalance = parseInt(u.reverseHex(response.result.stack[0].value));
            if (!isNaN(tokenBalance)) {
                state.balance.LoginToken = tokenBalance.toString();
            }
            if (state.balance.GAS !== '0' || state.balance.LoginToken == '1') {
                state.loggedIn = true
            }
        }
    }
}

const actions = {
    [SUBMIT_PRIVATEKEY]({ commit }, privatekey) {
        commit(SUBMIT_PRIVATEKEY, privatekey);
    }
}

const getters = {
    address: (state) => state.address,
}

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})