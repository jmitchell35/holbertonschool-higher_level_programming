const namePromise = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');

// Nested promises from fetch and response.json() => async function makes this more "linear"
console.log(namePromise
  .then((response) => {
    const responsePromise = response.json();
    responsePromise
      .then((result) => {
        document.getElementById('character').textContent = result.name;
      })
  })
);
