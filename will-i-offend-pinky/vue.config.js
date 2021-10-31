module.exports = {
  runtimeCompiler: true,
  pwa: {
    name: '我会冒犯***吗？',
    iconPaths: {
      favicon32: './icons/favicon-32x32.png',
      favicon16: './icons/favicon-16x16.png',
      appleTouchIcon: './icons/apple-touch-icon.png',
      maskIcon: './icons/safari-pinned-tab.svg',
      msTileImage: './icons/mstile-150x150.png'
    }
  },
  chainWebpack: config => {
    config
        .plugin('html')
        .tap(args => {
            args[0].title = "我会冒犯***吗？😅";
            return args;
        })
  }
}