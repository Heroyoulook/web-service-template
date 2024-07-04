<template>
  <div id="app">
    <AppNavbar />
    <div class="container mt-4">
      <!-- <ExampleAxiosComponent /> -->
    </div>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue'
// import ExampleAxiosComponent from './components/ExampleAxiosComponent.vue'

export default {
  name: 'App',
  components: {
    AppNavbar,
    // ExampleAxiosComponent
  }
}
</script>

<style>
@import '~bootstrap/dist/css/bootstrap.min.css';
/* Add any global styles here */
</style>
