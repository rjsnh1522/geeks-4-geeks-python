import Vue from 'vue'
import Vuex from 'vuex'
import SearchStore from "@/store/Search";

Vue.use(Vuex)

// Note before writing code in store modules..
// Actions are not be written until they are state related.
// Actions are not api calls.

export default new Vuex.Store({
    state: {
    },
    mutations: {
    },
    actions: {
    },
    modules: {
        SearchStore: SearchStore,
    }
})
