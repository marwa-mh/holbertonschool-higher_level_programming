#!/usr/bin/node

function factorial (n) {
  if (Number.isNaN(n) || n <= 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}
const { argv } = require('node:process');
const a = parseInt(argv[2]);

console.log(factorial(a));
