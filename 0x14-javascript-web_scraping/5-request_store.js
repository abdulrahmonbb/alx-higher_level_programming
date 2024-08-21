#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (_err, _res, body) {
  fs.writeFile(file, body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
