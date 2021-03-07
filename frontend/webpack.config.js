const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin')
const CompressionPlugin = require('compression-webpack-plugin')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const path = require('path')
const webpack = require('webpack')
const regeneratorRuntime = require("regenerator-runtime/path").path

const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const DJANGO_DIR = path.join(__dirname, '..', 'bud_band/static')
const DJANGO_BUILD_DIR = path.join(__dirname, '..', 'bud_band/static/dist')

process.traceDeprecation = true

const regRun = path.join(__dirname, '..', 'bud_band/static/src/js/index.jsx')
console.log('regrun is', regRun)
console.log('django dir', DJANGO_DIR)
console.log('django_build_dir', DJANGO_BUILD_DIR)
const django_config = {
  entry: {
    main: [regeneratorRuntime, path.join(__dirname, '..', 'bud_band/static/src/js/index.jsx')],
    vendor: ['react', 'react-dom', 'fixed-data-table', 'sortablejs', 'dashjs', 'fine-uploader', 'regenerator-runtime'],
  },
  output: {
    path: path.join(DJANGO_DIR, 'dist'),
    filename: '[name].js'
  },
  mode: IS_PRODUCTION ? 'production' : 'development',
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
    new ExtractTextPlugin({
      filename: '../../css/[name].css',
      disable: true,
      allChunks: true,
    }),
    new CleanWebpackPlugin([DJANGO_BUILD_DIR])
  ],
  resolve: {
    extensions: ['.js', '.json', '.jsx'],
    modules: [path.resolve(__dirname, 'node_modules'), 'node_modules'],
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        exclude: /node_modules/,
        options: {
          presets: [
            '@babel/preset-env',
            '@babel/react',
            {
              'plugins': ['@babel/plugin-proposal-class-properties']
            }
          ]
        }
      },
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader',
              options: {
                minimize: IS_PRODUCTION,
                sourceMap: IS_PRODUCTION,
              },
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: IS_PRODUCTION,
              },
            },
          ],
        }),
      },
      {
        test: /\.svg(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              name: 'assets/[contenthash].[ext]',
              limit: 80000,
              mimetype: 'image/svg+xml',
            },
          },
        ],
      },
      {
        test: /\.woff$|\.eot$|\.ttf$/,
        loader: 'file-loader',
      },
    ],
  },
}

module.exports = [django_config]
