#!/usr/bin/node

fs.readFile(process.argv[2], "utf8", function(err, data) { 
    console.log (data);
});