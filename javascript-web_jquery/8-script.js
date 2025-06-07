$(document).ready(function() {
    // Fetch data from SWAPI API
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Loop through each movie in the results array
            $.each(data.results, function(index, movie) {
                // Append each movie title as a list item to the UL#list_movies
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching movie data:', error);
        }
    });
});
