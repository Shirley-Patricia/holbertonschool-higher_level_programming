#!/usr/bin/node

const { argv } = require('process');

function factorial (a) {
  if (!a) {
    return 1;
  }
  if (a !== 0) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

const result = factorial(parseInt(argv[2]));
if (!argv[2]) {
  console.log(result);
}
if (argv[2] >= 0) {
  const result = factorial(parseInt(argv[2]));
  console.log(result);
}
