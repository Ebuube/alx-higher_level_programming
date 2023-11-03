// Say hello to everybody!

$(function () {
    $('INPUT#btn_translate').bind('click', function() {
        sayHello();
    });

    $('INPUT#language_code').on("keypress", function(event) {
        const enter_key = 13;

        if (event.which === enter_key) {
            sayHello();
        }
    });

    function sayHello(event) {
    const customUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $.ajax({
        url: customUrl + $('INPUT#language_code').val(),

        type: 'GET',

        dataType: 'json'
    })

        .done(function (json) {
        $('DIV#hello').text(`${json.hello}`);
        });
    };
  });
