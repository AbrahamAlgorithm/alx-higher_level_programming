#!/usr/bin/node

const request = require('request');
const file = process.argv[2];
request(file, function (err, response, body) {
  if (err) console.log(err);
  else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const film = films[i].characters;
      for (const j in film) {
        if (film[j].includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
