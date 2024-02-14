#!/usr/bin/node
const dict = require('./101-data.js').dict;
const sortdic = {};
for (const key in dict) {
  if (sortdic[dict[key]] === undefined) {
    sortdic[dict[key]] = [key];
  } else {
    sortdic[dict[key]].push(key);
  }
}
console.log(sortdic);
