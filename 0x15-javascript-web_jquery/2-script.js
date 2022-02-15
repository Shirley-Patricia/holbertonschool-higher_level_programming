#!/usr/bin/node
/** JavaScript script that updates the text color of the <header> element
* to red (#FF0000) when the user clicks on the tag DIV#red_header
* using JQuery API
*/

function readColor () {
  $('header').css('color', '#FF0000');
}
$(document).ready(function () {
  $('#red_header').on('click', readColor);
});
