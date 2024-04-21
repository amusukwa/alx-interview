#!/usr/bin/node

const request = require('request');

// Function to retrieve character details using a promise
function getCharacterDetails(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character);
      }
    });
  });
}

// Function to retrieve characters of a Star Wars movie
async function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  try {
    // Make a GET request to retrieve movie details
    const movieResponse = await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
    const characters = movieResponse.characters;

    // Retrieve character details in order and print their names
    for (const characterUrl of characters) {
      const character = await getCharacterDetails(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

// Check if Movie ID is provided as a command-line argument
if (process.argv.length !== 2) {
  console.error('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getCharacters(movieId);
}
