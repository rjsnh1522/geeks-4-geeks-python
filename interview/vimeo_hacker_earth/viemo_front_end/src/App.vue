<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import Search from './components/Search.vue'
import Header from './components/Header.vue'
export default {
  name: 'app',
  components: {
    Search,
    'app-header':Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin: 10px;
}
</style>
