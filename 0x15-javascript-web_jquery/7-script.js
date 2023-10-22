$.get("https://swapi-api.alx-tools.com/api/people", function(data){
    $("DIV#character").text(data.name);
});