/* global $ */
/**
 * This script tuggles the class of the `<header>` element when the user clicks
 */
$('DIV#toggle_header').click(function () {
  if ($(this).hasClass('red')) {
    $(this).toggleClass('green');
  } else {
    $(this).toggleClass('red');
  }
});
