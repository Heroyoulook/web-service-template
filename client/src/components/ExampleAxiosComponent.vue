<template>
  <div>
    <h1>API Data</h1>
    <pre>{{ info }}</pre>
  </div>
</template>

<script>
import axios from '../api/axios';

export default {
  name: 'ExampleAxiosComponent',
  data() {
    return {
      info: null,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/books/'); // '/api/some-endpoint' will be proxied
        this.info = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
