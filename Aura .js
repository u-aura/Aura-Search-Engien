// Aura.js
// This file links search functionality with the frontend

const search = require('./websitelink');

document.getElementById("searchButton").addEventListener("click", function() {
    const query = document.getElementById("searchInput").value;
    search(query);
});


const search = require('./websitelink');

document.getElementById("searchButton").addEventListener("click", function() {
    const query = document.getElementById("searchInput").value;
    search(query);
});
