#!/usr/bin/node
const data = require('./101-data').dict;

const result = {};

for (const key in data) {
  const occurrence = data[key];
  if (!result[occurrence]) {
    result[occurrence] = [];
  }
  result[occurrence].push(key);
}

console.log(result);
