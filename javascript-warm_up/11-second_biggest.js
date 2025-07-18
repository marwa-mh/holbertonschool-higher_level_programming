#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  } else {
    arr.sort((a, b) => b - a);
    return (arr[1]);
  }
}
const { argv } = require('node:process');

console.log(secondBiggest(argv.slice(2)));
