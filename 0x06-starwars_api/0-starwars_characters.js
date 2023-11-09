#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * Display one character name per line in the same order
 * as received from starwars api
 */

import request from 'request';
const movieId = process.argv[2] + '/';
const starwarsUrl = 'https://swapi-api.hbtn.io/api/films/';

request(starwarsUrl + movieId, async (err, _, body) => {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;

  // await for get requests and print as the response is comes
  for (const movcharacter of characters) {
    await new Promise((resolve, reject) => {
      request(movcharacter, (err, _, body) => {
        if (err) return console.error(err);

        // Display one character name per line in the same order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
