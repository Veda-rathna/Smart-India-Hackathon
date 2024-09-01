// Initialize the map
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 37.7749, lng: -122.4194 },
        zoom: 12,
    });

    // Add markers for each hospital
    const hospitals = [
        { name: "Hospital A", lat: 37.7859, lng: -122.4364 },
        { name: "Hospital B", lat: 37.7959, lng: -122.4064 },
        // Add more hospitals as needed
    ];

    hospitals.forEach((hospital) => {
        const marker = new google.maps.Marker({
            position: { lat: hospital.lat, lng: hospital.lng },
            map: map,
            title: hospital.name,
        });

        // Add an info window for each marker
        const infowindow = new google.maps.InfoWindow({
            content: `<p>${hospital.name}</p><p>Address: 123 Main St, Anytown, USA</p><p>Phone: 555-555-5555</p>`,
        });

        marker.addListener("click", () => {
            infowindow.open(map, marker);
        });
    });
}

// Update the number of beds for a hospital
function updateBeds(hospitalName) {
    const input = document.getElementById(`beds-${hospitalName.toLowerCase().replace(" ", "-")}`);
    const newValue = input.value;

    // Update the database or perform other logic here
    console.log(`Updated number of beds for ${hospitalName} to ${newValue}`);
}

// Initialize the map when the page loads
google.maps.event.addDomListener(window, "load", initMap);