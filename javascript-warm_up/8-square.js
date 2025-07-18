#!/usr/bin/node

const { argv } = require('node:process');
const size = argv[2];
if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
