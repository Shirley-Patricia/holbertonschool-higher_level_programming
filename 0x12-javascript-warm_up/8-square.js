#!/usr/bin/node

const { argv } = require('process');

let size;
let j;

if (!parseInt(argv[2])) {
  console.log('Missing size');
} else {
  for (size = 0; size < argv[2]; size++) {
    let row = '';
    for (j = 0; j < argv[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
