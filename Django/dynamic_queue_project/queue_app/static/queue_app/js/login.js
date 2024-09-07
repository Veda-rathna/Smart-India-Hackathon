// core/static/js/script.js

function toggleLogin(type) {
    const userLogin = document.getElementById('user-login');
    const adminLogin = document.getElementById('admin-login');
    
    if (type === 'user') {
        userLogin.classList.remove('hidden');
        adminLogin.classList.add('hidden');
    } else {
        userLogin.classList.add('hidden');
        adminLogin.classList.remove('hidden');
    }
}

function login(userType) {
    if (userType === 'admin') {
        document.getElementById('adminForm').submit();
    } else {
        document.getElementById('userForm').submit();
    }
}
