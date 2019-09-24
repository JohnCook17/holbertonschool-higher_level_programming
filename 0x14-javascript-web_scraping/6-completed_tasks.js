#!/usr/bin/node

const request = require('request');

request
  .get(process.argv[2], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const myDict = {};
      const data = JSON.parse(body);
      for (let index = 0; index < data.length; index++) {
        if (data[index].completed === true) {
          if (!myDict[data[index].userId.toString()]) {
            myDict[data[index].userId.toString()] = 0;
          }
          myDict[data[index].userId.toString()]++;
        }
      }
      console.log(myDict);
    }
  });
