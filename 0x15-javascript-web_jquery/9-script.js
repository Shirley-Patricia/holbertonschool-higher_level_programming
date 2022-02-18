#!/usr/bin/node
/** JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr 
 * and displays the value of hello from that fetch in the HTML tag DIV#hello.
*/

$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(Object.keys(data)[1]);
});
