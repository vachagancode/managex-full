import { ref } from 'vue'

const isAuthenticated = ref(false)

const changeAuthStatus = () => {
    isAuthenticated.value = true
    localStorage.setItem('AuthStatus', isAuthenticated.value)
}

const getAuthStatus = () => {
    const storedStatus = localStorage.getItem('AuthStatus');
    return storedStatus === 'true';
}

export { changeAuthStatus, getAuthStatus }