#!/usr/bin/node
/**
 *  Concats 2 files.
 */
const fs = require('fs');
// read data from the files
const sourceFile1Data = fs.readFileSync(process.argv[2], 'utf-8');
const sourceFile2Data = fs.readFileSync(process.argv[3], 'utf-8');
// write data to the destination file
fs.writeFileSync(process.argv[4], sourceFile1Data + sourceFile2Data, 'utf8');
