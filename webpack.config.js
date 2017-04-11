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
			}
		]
	}
}