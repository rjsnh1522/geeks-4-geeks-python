import Vue from 'vue'
import Vuex from 'vuex'

import SearchApi from '@/apis/search-api'

Vue.use(Vuex)

const SearchStore = {
    state: {
        bankAccountLists:[],
        bankAccountObj: null,
        id: null,
    },
    getters: {
        getBankAccountList: (state) => {
            return state.bankAccountLists
        },
        getBankAccountId: state => {
            return state.id
        },
        getBankAccount: state => {
            return state.bankAccountObj
        }
    },
    mutations: {
        SET_BANK_ACCOUNT_LIST (state, bankAccountLists) {
            state.bankAccountLists = bankAccountLists
        },
        SET_ID(state, id) {
            state.id = id
        },
        SET_BANK_ACCOUNT_OBJ (state, bankAccountObj) {
            state.bankAccountObj = bankAccountObj
        }

    },
    actions: {
        FETCH_ALL_ACCOUNTS: ({commit,dispatch}, params) => {
            console.log('called here', params)
            SearchApi.get_bank_accounts(params).then(res => {
                if(res.status === 200){
                    commit('SET_BANK_ACCOUNT_LIST', res.data)
                }
                console.log('resss of casee', res)
            }, reason => {
                console.log('ress of reason', reason)
            }).catch(err => {
                console.log('catch of case', err)
            })

        },
        FETCH_ACCOUNT: ({commit, dispatch, getters}, id) => {
            commit('SET_ID', id)
            SearchApi.get_bank_account(getters.getCaseId).then((response) => {
                commit('SET_CASE', response.data)
            })
        },
    },
    modules: {}
}

export default SearchStore
