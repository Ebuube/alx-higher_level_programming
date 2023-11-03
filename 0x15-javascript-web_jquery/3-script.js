$('DIV#red_header').bind('click', function () {
  if (!($('body header').hasClass('red'))) {
    $('body header').addClass('red');
  }
});
