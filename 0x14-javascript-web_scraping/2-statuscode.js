#!/usr/bin/node
cinst request = require('request');
const file = process.argv;
request(file[2], function (err, response) {
  if (err) console.log(err);
  else { console.log('code: ' + response.statusCode); }
}};
