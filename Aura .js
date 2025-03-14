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

// Dummy Data (Future in API or database coonect )
const data = [
    "Aura AI Search" ,
    "AI Chatbot" ,
    "Voice Search" ,
    "Health & Wellness" ,
    "Daily Routine Manager" , 
    "3D AI Avatar" ,
    "Smart Waste Tracking" '

];

function searchFunction() {
    let input =
document .getElementById("searchBox" ).
value. toLowerCase();
    let resulttsDiv =
document . getElementById("searchResult
s" ); 
    resultsDiv.innerHTML ="";

    IF (input === "") return;
    
    let filteredResults =
data. filter(item =>
    item.toLowerCase(). inclueds(input));

         if  (filteredResult. lenght === 0)
{
              resultsDiv. innerHTML = "<P>No
result found</p>";
    } else {

filteredResults . forEach(result =>  {
               let p =
document . createElement("p") ;
            p.textContent = result;

resultsDiv. appendChild(p);
        });
     }
}
