#!/usr/bin/node
const fs = require('fs');
const NameFile = process.argv[2];

if (NameFile) {
  fs.readFile(NameFile, 'utf8', (error, datos) => {
    if (error) {
      console.log(error);
    } else {
      console.log(datos);
    }
  });
}
