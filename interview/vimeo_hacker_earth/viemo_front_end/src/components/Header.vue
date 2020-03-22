<template>
    <el-container type="flex" :gutter="-20" class="header-view" style="flex-direction: column;">
        <el-row type="flex" class="logo-wrapper">
            <router-link to="#">Viemo</router-link>
        </el-row>
        <el-menu background-color="#F4F4F5" text-color="#807D8A" active-text-color="white" :router="true" class="el-menu-vertical main-menu" :collapse="isCollapse" :default-active="activeLink">
            <el-menu-item :index="this.$router.resolve({name: 'search'}).route.path">
                <span slot="title">Account Table </span>
            </el-menu-item>
            <el-menu-item :index="this.$router.resolve({name: 'chart'}).route.path">
                <span slot="title">Chart</span>
            </el-menu-item>
        </el-menu>
    </el-container>
</template>


<script>
    export default {
        name: 'Header',
        components: {
        },
        data () {
            return {
                isCollapse: false,
                activeLink: null,
            }
        },
        watch: {
            $route (to, from) {
                this.activeLink = to.path;
            }
        },
        mounted: function(){
            this.activeLink = this.$route.path;
        },
        methods: {
            logout () {
                this.$store.dispatch('AUTH_LOGOUT')
            }
        },
        created () {
        }
    }
</script>


<style lang="css">

</style>
