#!/usr/bin/node

const argCount = process.argv.length - 2;

if (argCount === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
