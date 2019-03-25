// Read more button
$(document).ready(function() {          
    $('.button-txt').each(function(){
        var dot_id = 'dots_' + $(this).attr('id');
        var more_id = 'more_' +$(this).attr('id');
        $(this).click(function(){
            if ($('#'+dot_id).css('display') === 'none'){
                $('#'+dot_id).css('display','inline');
                $('#'+more_id).css('display','none');
                $(this).text('Read more');
            }
            else {
                $('#'+dot_id).css('display','none');
                $('#'+more_id).css('display','inline');
                $(this).html('Read less');
            }
        });
    });
});

// Search Button on result page:
$('#searchBtn').click(function(){
    search();
});

// Press enter on q term:
$('#q').keydown(function(e){
	if (e.keyCode == 13) {
	 search()
	}
});

function search(){
    // Get query term:
    var q = $('#q').val();
    // Back to search form
    if (q == "" || q == null || q == undefined) {
		location.href='/';
    }
    // Redirect to new result page with query term:
    else {
        var string = '/query?q=' + q;
        location.href = string;
    }
}

// Modal image:
$(document).ready(function() {
    $('.modal').each(function(){
        var modal_id = '#' + $(this).attr('id');
        var img_id = '#img' + $(this).attr('id');
        var cap_id = '#cap' + $(this).attr('id');
        var md_img = '#mi' + $(this).attr('id');
        $(img_id).click(function(){
            $(modal_id).css('display','block');
            $(md_img).attr("src", $(img_id).attr('src'));
            $(cap_id).html($(img_id).attr('alt'));
            $('#q').css('display','none');
            $('#searchBtn').css('display','none');
        });
        $('.close').click(function(){
            $(modal_id).css('display','none');
            $('#q').css('display','block');
            $('#searchBtn').css('display','block');
        });
    });
});
