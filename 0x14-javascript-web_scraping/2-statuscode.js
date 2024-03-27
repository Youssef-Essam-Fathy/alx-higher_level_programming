#!/usr/bin/node

const { error } = require('console');
const request = require('request')

const url = process.argv[2];

request.get(url, (err, response, body) => {
    if (err)
});