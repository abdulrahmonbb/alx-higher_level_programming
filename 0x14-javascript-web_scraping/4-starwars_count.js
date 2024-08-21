#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line argument

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const wedgeMovies = movies.filter(movie => {
      return movie.characters.some(character => character.endsWith('18/'));
    });
    console.log(wedgeMovies.length);
  }
});
