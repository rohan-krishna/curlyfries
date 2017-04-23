// special jQuery Import
window.$ = window.jQuery = require('jquery');


// imports
var Quill = require('quill');
var QuillDelta = require('quill-delta');
var Delta = Quill.import('delta');
var Waves = require('node-waves');


// jQuery --------------------
$(document).ready(function() {
	
	// var quill = new Quill('#bodyInput', {
	// 	theme: 'bubble',
	// 	placeholder : "Compose an Epic!",
	// 	modules : {
	// 		toolbar: [['bold','italic','underline','strike'],[{ 'header' : [1,2,3] }],[{'list' : 'ordered'},{'list' : 'bullet'}],['link']]
	// 	}
	// });

	// var change = new Delta();
	
	// quill.on('text-change', function(delta) {
	// 	change = change.compose(delta);
	// 	console.log("Change detected!")
	// });

	// var activeStory = $('[name="story"]').val();

	// setInterval(function() {
	// 	if (change.length() > 0 && activeStory != 0 ) {
			
	// 		$.post('updatestory/', {
	// 			body: JSON.stringify(quill.getContents()),
	// 			csrfmiddlewaretoken : $('[name="csrfmiddlewaretoken"]').val(),
	// 			story : activeStory
	// 		});

	// 		change = new Delta();

	// 	}
	// },1500);
	
	// console.log("Hello World!");
	

	// Initialize Waves CSS
	Waves.init();
	Waves.attach('.wv-block', ['waves-block','waves-float']);
	Waves.attach('.wv-icon', ['waves-circle']);
});
// ------------------------------
// console.log("Hello World! ")