$("DIV#red_header").bind("click", function() {
    if ($("body header").hasClass("red")) {
        ;
    } else {
        $("body header").addClass("red");
    }
})