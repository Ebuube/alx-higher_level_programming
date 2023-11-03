// Say hello to everybody!

$(function () {
  $('INPUT#btn_translate').bind('click', function () {
    const customUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $.ajax({
      url: customUrl + $('INPUT#language_code').val(),

      type: 'GET',

      dataType: 'json'
    })

      .done(function (json) {
        $('DIV#hello').text(`${json.hello}`);
      });
  });
});
