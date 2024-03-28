#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Star Wars API URL
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
    if (error) {
        // If an error occurred, print the error message
        console.error(error);
    } else if (response.statusCode !== 200) {
        // If the request was not successful, print the status code
        console.error(`Request failed with status code ${response.statusCode}`);
    } else {
        // Parse the JSON response body
        const movieData = JSON.parse(body);

        // Print the title of the movie
        console.log(`${movieData.title}:`);

        // Loop through the characters and print their names
        movieData.characters.forEach(characterUrl => {
            request.get(characterUrl, (error, response, body) => {
                if (!error && response.statusCode === 200) {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                } else {
                    console.error(`Failed to fetch character data from ${characterUrl}`);
                }
            });
        });
    }
});

