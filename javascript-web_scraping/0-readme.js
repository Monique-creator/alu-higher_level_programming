#!/usr/bin/node
// Import the built-in file system module
const fs = require('fs');

// Get the file path from the first command line argument
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    // Print the error object if an error occurred
    console.log(error);
  } else {
    // Print the content of the file
    process.stdout.write(data);
  }
});
