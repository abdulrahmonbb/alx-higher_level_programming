#!/usr/bin/node
// Prints x times 'C is fun'

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  const n = Number(x);
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
