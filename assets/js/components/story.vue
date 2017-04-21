<template>
    <div>
        <div class="row justify-content-md-center">
        	<div class="col">
        		<form>
        			<input type="text" 
        					id="titleInput" 
        					name="title" 
        					class="title-input" 
        					placeholder="Inspire Yourself Today!" 
        					autofocus="autofocus" 
        					@change.once="createNewStory()" 
        					v-model="title">
        			<input type="hidden" name="body">
        			<div id="bodyInput" class="body-input"></div>
        		</form>
        	</div>
        </div>
    </div>
</template>

<script>
	export default {
		data() {
			return {
				title : ""
			}
		},
		methods : {
			createNewStory() {
				$.post("savenewstory", { title: this.title })
					.done(function(data) {
						alert("Data loaded: " + data.message)
					})
			}
		}
	}
</script>