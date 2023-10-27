#!/usr/bin/node
// Sort a dictionary of occurrences by user ids by occurrence
const dict = require('./100-data').dict;
const newDict = {};
for (const val of Object.values(dict)) {
	console.log(`key -> ${val}`);
}
