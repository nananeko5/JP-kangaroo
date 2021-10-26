module.exports = {
  assetsDir: 'static',
  devServer: {
      port:8888,
    proxy: {
        '^/back/': {
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            pathRewrite: { "^/back/": "/back/" },
            logLevel:'debug'
        }
    }
}
  
}
