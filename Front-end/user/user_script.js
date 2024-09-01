document.addEventListener('DOMContentLoaded', () => {
    const hospitals = [
        { name: 'Hospital A', beds: 20, distance: '2 km' },
        { name: 'Hospital B', beds: 5, distance: '5 km' },
        { name: 'Hospital C', beds: 3, distance: '7 km' }
        // You would fetch this data from the server in a real application
    ];

    const hospitalResults = document.getElementById('hospital-results');

    hospitals.forEach(hospital => {
        if (hospital.beds > 0) {
            const hospitalItem = document.createElement('div');
            hospitalItem.className = 'hospital-item';
            hospitalItem.innerHTML = `
                <span>${hospital.name} - ${hospital.beds} beds available</span>
                <span>${hospital.distance}</span>
            `;
            hospitalResults.appendChild(hospitalItem);
        }
    });
});
