#!/usr/bin/node

const { argv } = require('process');

let x;

if (!parseInt(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < argv[2]; x++) {
    console.log('C is fun');
  }
}
