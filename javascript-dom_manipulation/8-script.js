// helloDivElement not found => need to wait for DOM full load
document.addEventListener('DOMContentLoaded', () => {
  const helloDivElement = document.getElementById('hello');

  async function getHello() {
    try {
      const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
      const data = await response.json();
      helloDivElement.textContent = data.hello;
    } catch (error) {
      console.error('Error fetching character:', error);
      helloDivElement.textContent = `Error: ${error.message}`;
    }
  };

  getHello();
});
