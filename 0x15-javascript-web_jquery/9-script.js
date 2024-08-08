/* global $ */
/**
 * This script fetches from a URL and displays the value of `hello`
 * in the HTML tag `DIV#hello`.
 */
$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data, status) {
      $('DIV#hello').html(data.hello);
    });
});
