#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const args = argv.length;
const fs = require('fs');
const url = argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(argv[3], body, err => {
    if (args <= 2) {
      console.log(err);
    }
  });
});
