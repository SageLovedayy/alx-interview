#!/usr/bin/node

const https = require('https');
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movieID>');
  process.exit(1);
}

const movieID = process.argv[2];

if (isNaN(movieID) || movieID <= 0) {
  console.error('Error: <movieID> must be a positive number');
  process.exit(1);
}

const request = (url) => {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: new URL(url).hostname,
      path: new URL(url).pathname,
      method: 'GET'
    };

    const req = https.request(options, (res) => {
      let data = '';

      if (res.statusCode !== 200) {
        res.resume(); // Response data consumption to free up memory
        return reject(new Error(`Error: Received status code ${res.statusCode}`));
      }

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        if (!data.trim()) {
          return reject(new Error('Error: Received empty response'));
        }

        try {
          const parsedData = JSON.parse(data);
          resolve(parsedData);
        } catch (e) {
          reject(new Error(`Error parsing JSON: ${e.message}`));
        }
      });
    });

    req.on('error', (err) => {
      reject(new Error(`Error: ${err.message}`));
    });

    req.end();
  });
};

const fetchCharacters = async (movieID) => {
  try {
    const movieUrl = `${baseUrl}films/${movieID}/`;
    const movieData = await request(movieUrl);
    const characterUrls = movieData.characters;

    const characterPromises = characterUrls.map(url => request(url));
    const characters = await Promise.all(characterPromises);
    const characterNames = characters.map(character => character.name);

    return characterNames;
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
};

fetchCharacters(movieID).then((characterNames) => {
  characterNames.forEach(name => console.log(name));
}).catch((error) => {
  console.error('Error:', error.message);
  process.exit(1);
});
