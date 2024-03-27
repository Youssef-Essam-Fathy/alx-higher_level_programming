#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const swApi = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get(swApi, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});
