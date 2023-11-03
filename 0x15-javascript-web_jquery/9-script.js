// Using the core $.ajax() method
$.ajax({
    // The URL for the request
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  
    type: 'GET',
  
    dataType: 'json'
  })
  
.done(function (json) {
    // Say Hello in French
    $("DIV#hello").text(`${json.hello}`);
});
