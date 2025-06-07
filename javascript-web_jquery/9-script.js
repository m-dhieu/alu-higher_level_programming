$(document).ready(function() {
    $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        method: 'GET',
        success: function(response) {
            $('#hello').text(response.hello);
        },
        error: function(xhr, status, error) {
            $('#hello').text('Error fetching hello: ' + error);
        }
    });
});
