#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], 'utf8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.error(err);
  }
});
