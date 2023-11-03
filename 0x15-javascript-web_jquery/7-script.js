// Using the core $.ajax() method
$.ajax({
  // The URL for the request
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',

  type: 'GET',

  dataType: 'json'
})

  .done(function (json) {
    $('DIV#character').text(json.name);
  });
