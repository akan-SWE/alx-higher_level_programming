/* global $ */

$(function () {
  // Event listener for button click
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val(); // Get the value inside the event handler
    $.get(url + lang, function (data, status) {
      if (status === 'success') {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
