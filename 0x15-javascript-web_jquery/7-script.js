/* global $ */
/**
 * This script fetches the character `name` from a URL and adds it
 * to the HTML tag `DIV#character`
 */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data, status) {
      if (status === 'success') {
        $('DIV#character').html(data.name);
      }
    });
});
