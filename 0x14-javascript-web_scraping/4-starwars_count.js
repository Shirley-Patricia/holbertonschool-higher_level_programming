#!/usr/bin/node

const request = require('request');
const url = ('https://swapi-api.hbtn.io/api/films/');

request(url, (error, response, body) => {
  if (error) console.log(error);
  const bodies = JSON.parse(body);

  let count = 0;
  let i;
  let j;

  for (i in bodies.results) {
    const len = bodies.results[i].characters.length;
    for (j = 0; j < len; j++) {
      const sentence = bodies.results[i].characters[j];
      if (sentence.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
