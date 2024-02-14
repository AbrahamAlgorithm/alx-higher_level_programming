#!/usr/bin/node
const list = require('./100-data.js').list;
const arr = list.map((element, index) => element * index);
console.log(list);
console.log(arr);
