import { mapData } from './neighbourhoods.js'

let jsonData = mapData;

window.onload = function () {
    const myMap = L.map('mapBox').setView([43.720, -79.340505], 11);
                
    const defaultTileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(myMap);

    L.geoJSON(jsonData, {
        onEachFeature: function (feature, layer) {
        layer.bindPopup('</h1>'+feature.properties.HOOD+'</h1>');
    }
    }).addTo(myMap);

}