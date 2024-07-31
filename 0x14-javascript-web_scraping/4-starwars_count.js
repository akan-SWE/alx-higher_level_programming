#!/usr/bin/node
/**
 * This script makes a GET request to the Star wars API
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');

const wedgesAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(wedgesAntillesUrl, { json: true }, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(response.body.films.length);
  }
});
