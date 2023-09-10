#!/usr/bin/node
const request = require("request");

function getMovieCharacters(movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error("Error:", error);
      return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error("Error:", error);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error("Please provide a Movie ID as the first positional argument.");
} else {
  getMovieCharacters(movieId);
}
