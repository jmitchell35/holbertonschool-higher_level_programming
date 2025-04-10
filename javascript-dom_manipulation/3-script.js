document.getElementById('toggle_header').addEventListener('click', () => {
  const headerElement = document.querySelector('header');
  if (headerElement.classList.contains('red')) {
    headerElement.classList.replace('red', 'green');
  } else {
    headerElement.classList.replace('green', 'red');
  }
});
