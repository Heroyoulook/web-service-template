const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      // Proxy requests starting with /api to the target server
      '/api': {
        target: 'http://localhost:5000/api', // Replace with your target server
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
})
