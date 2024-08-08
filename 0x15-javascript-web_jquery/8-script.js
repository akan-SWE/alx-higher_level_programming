/* global $ */
/**
 * This script fetches and list the `title` for all movies from a URL
 */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      data.results.forEach(function (item) {
        $('UL#list_movies').append(`<li>${item.title}</li>`);
      });
    });
});
