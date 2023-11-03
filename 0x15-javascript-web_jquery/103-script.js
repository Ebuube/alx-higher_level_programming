// And press Enter
// Prints How to say "Hello" depending on the language

$(function () {
  $('INPUT#btn_translate').bind('click', function () {
    sayHello();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    const enterKey = 13;

    if (event.which === enterKey) {
      sayHello();
    }
  });

  function sayHello (event) {
    const customUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $.ajax({
      url: customUrl + $('INPUT#language_code').val(),

      type: 'GET',

      dataType: 'json'
    })

      .done(function (json) {
        $('DIV#hello').text(`${json.hello}`);
      });
  }
});
