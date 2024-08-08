/* global $ */
/**
 * This script that adds, removes and clears LI elements from a list
 * when the user clicks.
 */
$(function () {
  // listen for click event on `DIV#add_item` and adds an item
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // listen for click event on `DIV#remove_item` and remove an item
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
  // listen for click event on `DIV#clear_list` and removes all element
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
