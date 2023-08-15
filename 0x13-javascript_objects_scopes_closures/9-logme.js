#!/usr/bin/nodejs

let argumentsPrinted = 0;

exports.logMe = function (item) {
  console.log(`${argumentsPrinted}: ${item}`);
  argumentsPrinted++;
};
