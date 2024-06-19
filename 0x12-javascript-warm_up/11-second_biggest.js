#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.

const argCount = process.argv.length - 2;

if (argCount <= 1) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
