#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the URL from the first command line argument
const url = process.argv[2];

// Perform a GET request to the provided URL
request(url, function (error, response) {
  if (error) {
    // Print the error if the request fails
    console.log(error);
  } else {
    // Print the status code of the response
    console.log('code: ' + response.statusCode);
  }
});

