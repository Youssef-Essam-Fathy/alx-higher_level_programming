#!/usr/bin/node

const request = require('request');

const swApi = process.argv[2];
let num = 0;

request.get(swApi, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }
  const filmsData = JSON.parse(body).results;
  filmsData.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(18)) {
        num += 1;
      }
    });
  });
  console.log(num);
});
