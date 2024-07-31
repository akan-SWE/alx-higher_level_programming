#!/usr/bin/node

/**
 * This script makes a GET request to the Star wars API and
 * prints the title of a Star Wars movie where the episode number matches
 * a given integer passed as argument
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, { json: true }, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(response.body.title);
  }
});
