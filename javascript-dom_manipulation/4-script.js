const uListElement = document.getElementById('add_item');
uListElement.addEventListener('click', () => {
  const listItem = document.createElement('li');
  listItem.textContent = 'Item';
  document.getElementsByClassName('my_list').item(0).appendChild(listItem);
});
