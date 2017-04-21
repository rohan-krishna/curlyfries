var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var webpack = require('gulp-webpack');
var notify  = require('gulp-notify');
// var babel = require('gulp-babel');
// var uglify = require('gulp-uglify');

gulp.task('build-js', function() {
	return gulp.src('build.js')
			.pipe(webpack( require('./webpack.config.js') ))
			.pipe(notify("Webpack compiled!"))
			.pipe(gulp.dest('household/static/household/js'));
});

gulp.task('build-css', function() {
	return gulp.src('assets/sass/**/*.scss')
		.pipe(sourcemaps.init())
		.pipe(sass())
		.pipe(sourcemaps.write())
		.pipe(notify("Styles has been compiled."))
		.pipe(gulp.dest('household/static/household/css'));
});

gulp.task('watch',['build-js','build-css'] ,function() {
	gulp.watch('assets/sass/**/*.scss', ['build-css']);
	gulp.watch('build.js',['build-js']);
});