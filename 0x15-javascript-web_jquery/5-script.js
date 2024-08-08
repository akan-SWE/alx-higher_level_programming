/* global $ */
/**
 * Adds a `<li>` element to a list when the user clicks on tag `DIV#add_item`
 */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
