// special jQuery Import
window.$ = window.jQuery = require('jquery');


// imports
var Quill = require('quill');
var QuillDelta = require('quill-delta');
var Delta = Quill.import('delta');
var Waves = require('node-waves');

 
import UIKit from 'uikit';
import UIKitIcons from 'uikit/dist/js/uikit-icons';

UIKit.use(UIKitIcons);

// Import Portfolio App JS
require('./portfolio.js');  

// jQuery --------------------
$(document).ready(function() {

	// Initialize Waves CSS
	Waves.init();
	Waves.attach('.wv-block', ['waves-block','waves-float']);
	Waves.attach('.wv-icon', ['waves-circle']); 
});
// ------------------------------
// console.log("Hello World! ")