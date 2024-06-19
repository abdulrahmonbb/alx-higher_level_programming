#!/usr/bin/node
// Computes and prints a factorial
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(n)));
