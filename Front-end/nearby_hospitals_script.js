let userLatitude, userLongitude;

// List of hospitals in Tamil Nadu with their coordinates
const hospitals = [
    {name: "Apollo Hospital, Chennai", latitude: 13.0593, longitude: 80.2473},
    {name: "Kauvery Hospital, Chennai", latitude: 13.0347, longitude: 80.2389},
    {name: "PSG Hospitals, Coimbatore", latitude: 11.0227, longitude: 76.9791},
    {name: "Ganga Hospital, Coimbatore", latitude: 11.0173, longitude: 76.9585},
    {name: "MIOT International, Chennai", latitude: 13.0107, longitude: 80.1846},
    {name: "SRM Hospital, Kattankulathur", latitude: 12.8225, longitude: 80.0449}
    // Add more hospitals as needed
];

// Get the user's current location
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, handleError);
    } else {
        document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
    }
}

// Show the user's position and find the nearest hospital
function showPosition(position) {
    userLatitude = position.coords.latitude;
    userLongitude = position.coords.longitude;

    document.getElementById("location").innerHTML =
        "Latitude: " + userLatitude + " Longitude: " + userLongitude;

    findNearestHospital(userLatitude, userLongitude);
}

// Haversine formula to calculate the distance between two points
function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Radius of the Earth in km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c;
    return distance;
}

// Find the nearest hospital from the user's location
function findNearestHospital(userLat, userLon) {
    let nearestHospital = null;
    let minDistance = Infinity;

    hospitals.forEach(hospital => {
        const distance = getDistance(userLat, userLon, hospital.latitude, hospital.longitude);
        if (distance < minDistance) {
            minDistance = distance;
            nearestHospital = hospital;
        }
    });

    if (nearestHospital) {
        document.getElementById("hospital-info").innerHTML =
            "Nearest hospital is " + nearestHospital.name +
            " which is " + minDistance.toFixed(2) + " km away.";
    } else {
        document.getElementById("hospital-info").innerHTML = "No hospitals found.";
    }
}

// Handle errors in getting the user's location
function handleError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            document.getElementById("location").innerHTML = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            document.getElementById("location").innerHTML = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            document.getElementById("location").innerHTML = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            document.getElementById("location").innerHTML = "An unknown error occurred.";
            break;
    }
}
