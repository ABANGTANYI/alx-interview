#!/usr/bin/env node

// Script to fetch and display characters of a Star Wars movie based on Movie ID using the Star Wars API

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to fetch movie details
request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
        const film = JSON.parse(body);
        const characters = film.characters;

        // Fetch details of each character in the movie
        characters.forEach(characterUrl => {
            request(characterUrl, (err, resp, characterBody) => {
                if (!err && resp.statusCode === 200) {
                    const character = JSON.parse(characterBody);
                    console.log(character.name);
                } else {
                    console.log('Error fetching character details');
                }
            });
        });
    } else {
        console.log('Error fetching movie details');
    }
});
