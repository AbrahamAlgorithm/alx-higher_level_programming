const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Star Wars API URL for films
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the Star Wars API for films
request.get(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode !== 200) {
        console.error(`Request failed with status code ${response.statusCode}`);
    } else {
        const filmData = JSON.parse(body);
        const charactersUrls = filmData.characters;

        // Function to fetch character data
        const fetchCharacter = (url) => {
            return new Promise((resolve, reject) => {
                request.get(url, (error, response, body) => {
                    if (!error && response.statusCode === 200) {
                        const characterData = JSON.parse(body);
                        resolve(characterData.name);
                    } else {
                        reject(`Failed to fetch character data from ${url}`);
                    }
                });
            });
        };

        // Fetch character data for each character URL
        Promise.all(charactersUrls.map(url => fetchCharacter(url)))
            .then(characterNames => {
                // Print character names
                characterNames.forEach(name => console.log(name));
            })
            .catch(error => {
                console.error(error);
            });
    }
});

