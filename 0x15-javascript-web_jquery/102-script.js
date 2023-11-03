// Say hello to everybody!

$(function() {
    $("INPUT#btn_translate").bind("click", function() {
        const custom_url = "https://hellosalut.stefanbohacek.dev/?lang=";
        $.ajax({
            url: custom_url + $("INPUT#language_code").val(),

            type: "GET",

            dataType: "json"
        })

        .done(function (json) {
            $("DIV#hello").text(`${json.hello}`);
        })
    })
})