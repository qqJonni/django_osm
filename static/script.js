// var greenIcon = L.icon({
//     iconUrl: 'static/leaf-green.png',
//     shadowUrl: 'static/leaf-shadow.png',
//
//     iconSize:     [38, 95], // size of the icon
//     shadowSize:   [50, 64], // size of the shadow
//     iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
//     shadowAnchor: [4, 62],  // the same for the shadow
//     popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
//     });
//
//
//         var map = L.map('map').setView([41.6941, 44.8337], 8);
//         L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
//         maxZoom: 19,
//         attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
//         }).addTo(map);
//
//         let station = JSON.parse(document.getElementById('stations_json').textContent)
//
//         //добавляем другие точки на карте, которые там есть
//         station.forEach(station => {
//             L.marker([station.latitude, station.longitude], {icon: greenIcon}).addTo(map)
//         })