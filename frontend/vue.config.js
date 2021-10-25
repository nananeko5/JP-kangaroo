module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: {
        '^/server': {
            target: 'http://localhost:5000',
            changeOrigin: true
        }
    }
}
  
}
