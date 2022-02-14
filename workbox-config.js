module.exports = {
	globDirectory: 'src/',
	globPatterns: [
		'**/*.{js,css,png,html}'
	],
	swDest: 'src/sw.js',
	ignoreURLParametersMatching: [
		/^utm_/,
		/^fbclid$/
	]
};