$(function(){
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        type: "GET",
        success: function(data){
            $.each(data.results, function(i, movie){
                $("<li>").text(movie.title).appendTo("UL#list_movies");
            })
        }
    })
});