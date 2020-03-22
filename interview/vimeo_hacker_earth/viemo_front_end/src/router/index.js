import Vue from 'vue'
import VueRouter from 'vue-router'
import Search from "../components/Search";
import Chart from "../components/Chart";

Vue.use(VueRouter)
const routes = [
    {
        path: '/',
        name: 'search',
        component: Search
    },
    {
        path: '/chart',
        name: 'chart',
        component: Chart
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})


export default router
