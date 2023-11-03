// Using the core $.ajax() method
$.ajax({
  // The URL for the request
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',

  type: 'GET',

  dataType: 'json'
})

  .done(function (json) {
    // List the title for all movies
    for (const film of json.results) {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    }
  });
