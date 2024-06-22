#!/usr/bin/node
const dict = require('./101-data').dict;

// computes a dictionary of user ids by occurrence.
const userIdOccurrence = {};
for (const key in dict) {
  const value = dict[key];
  if (!(value in userIdOccurrence)) userIdOccurrence[value] = [];
  userIdOccurrence[value].push(key);
}
console.log(userIdOccurrence);
