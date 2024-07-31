#!/usr/bin/node
/**
 * Make a GET request to the URL pased as argument and display the
 * status code
 */

const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
