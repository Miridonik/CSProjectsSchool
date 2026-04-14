$(document).ready(function () {
    
    $('#regForm').on('submit', function () {
        erCode = 0;
        if ($('#name').val().trim() === '') {
            erCode = 1;
        }
        if(erCode == 0){
        $.ajax({
            URL: '/register_user',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                name: $('#name').val().trim(),
                password: $('#pass1').val(),
                mail: $('#mail').val()
            })
        })
    }
    })
    
})