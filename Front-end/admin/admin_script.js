function updateBeds(hospitalName) {
    const inputId = `beds-${hospitalName.toLowerCase().replace(/\s+/g, '-')}`;
    const beds = document.getElementById(inputId).value;
    alert(`Updated ${hospitalName} to have ${beds} beds available.`);
    
    // You would send the new bed count to the server here
}
