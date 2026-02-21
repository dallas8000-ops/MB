// about.js - Custom JS for About page

document.addEventListener('DOMContentLoaded', function() {
    console.log("About page loaded!");
    // Example: Change the color of the h1 after 1 second
    setTimeout(function() {
        var h1 = document.querySelector('h1');
        if (h1) {
            h1.style.color = 'teal';
        }
    }, 1000);
});
