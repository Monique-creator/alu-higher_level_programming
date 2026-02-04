#!/usr/bin/node
// Import the built-in file system module
const fs = require('fs');

// Get file path and content from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file using utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    // Print the error object if writing fails
    console.log(error);
  }
});
