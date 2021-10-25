module.exports = {
  assetsDir: 'static',
  devServer: {
      port:8888,
    proxy: {
        '^/back/': {
            target: 'http://localhost:5000',
            changeOrigin: true,
            pathRewrite: { "^/back/": "/back/" },
            logLevel:'debug'
        }
    }
}
  
}
