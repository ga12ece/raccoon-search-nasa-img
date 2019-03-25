$('#detailBtn').click(function(){
    if ($('#detailbox').css('display') === 'none'){
        $('#detailbox').css('display','block');
        $('#detailBtn').html('Show less');
    }
    else {
        $('#detailbox').css('display','none');
        $('#detailBtn').html('More details');
    }
});

var start = 1958;
var end = new Date().getFullYear();
var option = '<option selected></option>'
for(var year= start; year <= end; year++){
    option += '<option value="' + year.toString() + '">' + year.toString() + '</option>' 
}

$('#year_start').html(option)
$('#year_end').html(option)
