var webpack = require('webpack');

module.exports = {
	entry: './build.js',

	output: {
		filename : 'build.js'
	},

	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loader : 'babel-loader',
				query: {
					presets: ['es2015']
				}
			},
			{
				test: /\.vue$/,
				loader: 'vue'
			}
		]
	},
	plugins: [
	    new webpack.ProvidePlugin({
	      $: 'jquery', jQuery: 'jquery',
	      Tether: 'tether', tether: 'tether'
	    }),
	],
	vue: {
		loaders: {
			js: 'babel-loader'
		}
	},
	resolve: {
		alias: {
			vue: 'vue/dist/vue.js'
		}
	}
}