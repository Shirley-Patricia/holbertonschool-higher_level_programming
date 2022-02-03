#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const bodies = JSON.parse(body);

  let count = 0;
  for (const i in bodies.results) {
    const len = bodies.results[i].characters.length;
    for (let j = 0; j < len; j++) {
      const sentence = bodies.results[i].characters[j];
      if (sentence.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
