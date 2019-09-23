#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let results = 0;
  for (i in list) {
    if (list[i] === searchElement) {
      results++;
    }
    i++;
  }
  return results;
};
