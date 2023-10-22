$(function(){
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        type: "GET",
        success: function(data){
            $("DIV#hello").text(data.hello);
        }
    })
});