#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = ('https://swapi-api.hbtn.io/api/films/' + argv[2]);

request(url, (error, response, body) => {
  if (error) console.log(error);
  const bod = JSON.parse(body);
  console.log(bod.title);
});
