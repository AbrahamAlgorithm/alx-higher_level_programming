$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (film) {
  $('DIV#character').text(film.name);
});
