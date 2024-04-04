$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (film) {
  $res = film.results
  $.each(res, function(i, v) {
    $('DIV#character').append(`<li>${v.title}</li>`);
  })
});
