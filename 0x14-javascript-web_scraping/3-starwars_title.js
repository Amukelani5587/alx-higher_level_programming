#!/usr/bin/node

const request = require('request');

const Https = 'https://swapi-api.hbtn.io/api/films/';
request(Https + process.argv[2], function (error, response, body) {
  if (error) return (console.error('error', error));
  console.log(JSON.parse(body).title);
});
