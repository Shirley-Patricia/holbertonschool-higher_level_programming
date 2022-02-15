#!/usr/bin/node

function readColor () {
  $('header').css('color', '#FF0000');
}
$(document).ready(function () {
  $('#red_header').on('click', readColor);
});
