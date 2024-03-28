#!/usr/bin/node
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
    if (error) {
        // If an error occurred, print the error message
        console.error(error);
    } else if (response.statusCode !== 200) {
        // If the request was not successful, print the status code
        console.error(`Request failed with status code ${response.statusCode}`);
    } else {
        // Parse the JSON response body
        const todos = JSON.parse(body);

        // Create an object to store the number of completed tasks for each user ID
        const completedTasksByUserId = {};

        // Loop through the todos and count the number of completed tasks for each user ID
        todos.forEach(todo => {
            if (todo.completed) {
                if (completedTasksByUserId[todo.userId]) {
                    completedTasksByUserId[todo.userId]++;
                } else {
                    completedTasksByUserId[todo.userId] = 1;
                }
            }
        });

        // Print the object containing the number of completed tasks for each user ID
        console.log(completedTasksByUserId);
    }
});

