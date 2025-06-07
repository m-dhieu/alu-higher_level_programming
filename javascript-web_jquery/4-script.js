$(document).ready(function() {
    // When the user clicks on the element with ID toggle_header
    $('#toggle_header').click(function() {
        // Check if header has class red
        if ($('header').hasClass('red')) {
            // If it has class red, remove it and add green
            $('header').removeClass('red').addClass('green');
        } else {
            // If it has class green, remove it and add red
            $('header').removeClass('green').addClass('red');
        }
    });
});
