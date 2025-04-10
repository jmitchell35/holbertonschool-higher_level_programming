const ulElement = document.getElementById('list_movies');

// The async way
async function displaySwMoviesList() {
  try { // replaces promises nesting
    // First resolve
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    // Second
    const data = await response.json();
    // console.log(data) to see data structure
    for (movie of data.results) {
      const liElement = document.createElement('li');
      liElement.textContent = movie.title;
      ulElement.appendChild(liElement);
    };
  } catch (error) {
    console.error('Error fetching character:', error);
    ulElement.textContent = `Error: ${error.message}`;
  }
};

displaySwMoviesList();
