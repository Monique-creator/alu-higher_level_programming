#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterID = '18';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const movie of results) {
      for (const character of movie.characters) {
        if (character.includes('/' + characterID + '/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
