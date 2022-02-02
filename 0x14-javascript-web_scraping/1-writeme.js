#!/usr/bin/node

const { argv } = require('process');
const args = argv.length;
const fs = require('fs');
const content = argv[3];

fs.writeFile(argv[2], content, err => {
  if (args <= 2) {
    console.error(err);
  }
});
