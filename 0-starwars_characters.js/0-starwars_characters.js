#!/usr/bin/node

const request = require('request');

// Function to retrieve characters of a Star Wars movie
function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  // Make a GET request to retrieve movie details
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const movie = JSON.parse(body);
      const characters = movie.characters;
      
      // Print character names
      characters.forEach((characterUrl) => {
        // Make a GET request to retrieve character details
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

// Check if Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getCharacters(movieId);
}

