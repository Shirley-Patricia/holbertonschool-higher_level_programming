#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log('code: ' + response.statusCode);
});
