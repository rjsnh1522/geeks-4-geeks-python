import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import store from './store'
import router from './router'
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en'


import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Vuex)
Vue.use(ElementUI, { locale })
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
