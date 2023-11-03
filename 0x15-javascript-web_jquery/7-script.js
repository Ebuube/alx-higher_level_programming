// Using the core $.ajax() method
$.ajax({
    // The URL for the request
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",

    type: "GET",

    dataType: "json",
})

.done(function(json) {
    $("DIV#character").text(json.name);
})

.fail(function(xhr, status, errorThrown) {
    alert("The request failed!");
    console.log("Error: " + errorThrown);
    console.log("Status: " + status);
    console.dir(xhr);
})