#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(url, function (_err, _res, body) {
  const data = JSON.parse(body);
  console.log(data.title);
});
