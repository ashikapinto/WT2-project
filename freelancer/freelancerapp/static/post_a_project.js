$(function(){
	$('form').on('submit', function(e){
		e.preventDefault():
		$.ajax({
			url: $(this).attr('action'),
			method: $(this).attr('method'),
			success: function(){ $('post_project').html}
		});
	});
});
