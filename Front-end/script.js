function toggleLogin(role) {
    const userLogin = document.getElementById('user-login');
    const adminLogin = document.getElementById('admin-login');

    if (role === 'admin') {
        userLogin.classList.add('hidden');
        adminLogin.classList.remove('hidden');
    } else {
        adminLogin.classList.add('hidden');
        userLogin.classList.remove('hidden');
    }
}

function login(role) {
    const username = document.getElementById(`${role}-username`).value;
    const password = document.getElementById(`${role}-password`).value;


    alert(`Logged in as ${role}: ${username}`);
}
