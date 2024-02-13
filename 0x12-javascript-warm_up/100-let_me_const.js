#!/usr/bin/node
const fs = require('fs');

const newValue = 333;

const script = `
const myVar = ${newValue};
`;

fs.writeFileSync('modifiedScript.js', script);

