$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$('#LoginButton').click(function(){
    $.ajax({
        url: '/user_api/login/',
        method: 'post',
        dataType: 'html',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        data: {email: $('#emailLoginField').value,
               password: $('#passwordLoginField').value},
        success: function(data){
            console.log(data);
        },
        fail: function(data) {
        console.log(data)
        }
    });
})