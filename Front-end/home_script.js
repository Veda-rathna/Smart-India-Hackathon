// Simulate getting the username and role from the server or session
const username = "Admin"; // Replace with dynamic data in a real application
const role = "admin"; // This should be dynamically set based on the user's actual role

document.getElementById('welcome-message').innerText = `Welcome, ${username}`;

// Function to redirect based on role
function redirectBasedOnRole() {
    if (role === "admin") {
        window.location.href = "./admin/admin_dashboard.html";
    } else if (role === "user") {
        window.location.href = "./user/user_dashboard.html";
    } else {
        console.error("Unknown role:", role);
    }
}

