$(document).ready(function(){
    $('.delete-row').prop('disabled', true);

    $( "form" ).on( "submit", function( event ) {
        event.preventDefault();
        let rows = $('#field-container').children();
        let data = [];
        let isInvalid = false;

        $.each(rows, function(i, row){
            let _book_name = $(row).find('input[name=book_name]');
            let _duration = $(row).find('input[name=duration]');
            let d = {};
            d.book_name = _book_name.val();
            d.duration = _duration.val();
            data.push(d);
            if(isNullOrEmpty(_book_name) || !isNumber(_duration)){
                isInvalid = true;
            }
        });

        // alert(JSON.stringify(data));
        //alert(isInvalid);
        if(!isInvalid){
            calculate(data);
        }
    });

    $('.add-row').click(function(){
        let cloneFields = $('.clone').clone()[0];
        $(cloneFields).find('input[name=book_name]').val('');
        $(cloneFields).find('input[name=duration]').val('');
        $(cloneFields).find('input[name=book_name]').attr('class', '');
        $(cloneFields).find('input[name=duration]').attr('class', '');
        $('#field-container').append(cloneFields);
        
        $('.delete-row').prop('disabled', false);
        $('.delete-row').click(deleteRow);
        $('input[name=book_name]').keyup(keypress_book_name);
        $('input[name=duration]').keyup(keypress_duration);
    });

    $('.delete-row').click(deleteRow);
    $('input[name=book_name]').keyup(keypress_book_name);
    $('input[name=duration]').keyup(keypress_duration);
});

function deleteRow(){
    if($('#field-container').children().length==1){
        $(this).prop('disabled', true);
    }
    else{    
        $(this).prop('disabled', false);
        $(this).parents('.clone').remove();
    }
}

function keypress_book_name(){
    isNullOrEmpty($(this));
}

function keypress_duration(){
    isNumber($(this));
}

function isNullOrEmpty(obj){
    if($(obj).val()===''){
        $(obj).attr('class', 'invalid');
        $(obj).siblings("span").attr('data-error', "can't be empty");
        return true;
    }
    else{
        $(obj).attr('class', '');
        return false;
    }
}

function isNumber(obj){
    if($(obj).val()===''){
        $(obj).attr('class', 'invalid');
        $(obj).siblings("span").attr('data-error', "can't be empty");
        return false;
    }
    else if($(obj).val().match(/^(?=.*\D).+$/)){
        $(obj).attr('class', 'invalid');
        $(obj).siblings("span").attr('data-error', 'only digit');
        return false;
    }
    else if($(obj).val()==0){
        $(obj).attr('class', 'invalid');
        $(obj).siblings("span").attr('data-error', "can't be 0");
        return false;
    }
    else if($(obj).val()>90){
        $(obj).attr('class', 'invalid');
        $(obj).siblings("span").attr('data-error', "Can't exceed 90");
        return false;
    }
    else{
        $(obj).attr('class', '');
        return true;
    }
}


function calculate(data){
    $.ajax({
        url: '/calculate',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function (result) {
            $('tbody').empty();
            $.each(result['data'], function(i, v){
                let tr = '<tr>'+
                '<td>'+v['book_name']+'</td>'+
                '<td>'+v['duration']+'</td>'+
                '<td>&#8377; '+v['total']+'</td>'+
                '</tr>';

                $('tbody').append(tr);
            });

            $('tfoot').find('th').eq(2).html("&#8377; "+result['grand_total']);
            var instance = M.Modal.getInstance($('#receipt_model'));
            instance.open();
        },
        data: JSON.stringify(data)
    });
}