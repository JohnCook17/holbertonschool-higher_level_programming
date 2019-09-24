#!/usr/bin/node

const request = require('request');

request
  .get(process.argv[2], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let count = 0;
      let i = 0;
      let film = JSON.parse(body).results[i];
      for (const episode in film) {
        film = JSON.parse(body).results[i];
        if (film && episode) {
          const data = film.characters;
          for (const character in data) {
            if (data[character] === 'https://swapi.co/api/people/18/') {
              count++;
            }
          }
        }
        i++;
      }
      console.log(count);
    }
  });
