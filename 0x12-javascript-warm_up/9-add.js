#!/usr/bin/node
// Prints the addition of two integers

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];

  console.log(parseInt(a) + parseInt(b));
}

add();
