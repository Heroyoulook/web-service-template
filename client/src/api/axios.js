import axios from 'axios';

// Create an axios instance
const axiosInstance = axios.create({
  baseURL: '/api', // This base URL should match the proxy configuration in vue.config.js
  timeout: 1000, // Set a timeout for requests
  headers: { 'Content-Type': 'application/json' } // Set default headers
});

// Add a request interceptor
axiosInstance.interceptors.request.use(
  function (config) {
    // Do something before request is sent, such as adding auth token
    // config.headers.Authorization = `Bearer ${store.state.token}`;
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
axiosInstance.interceptors.response.use(
  function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    return response;
  },
  function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Handle response errors
    return Promise.reject(error);
  }
);

export default axiosInstance;
