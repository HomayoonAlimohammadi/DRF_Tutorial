// to run this html head to this directory and:
// python -m http.server 8111 


const loginForm = document.getElementById('login-form')
const baseEndpoint = 'http://localhost:8000/api'

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {

    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: bodyStr
    }
    console.log(bodyStr)
    fetch(loginEndpoint, options)
    .then(response => {
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err => {
        console.log(err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback()
    }
}

function getProductList() {
    const productEndpoint = `${baseEndpoint}/product/`
    const productDiv = document.getElementById('product-list')
    const options = {
        method: 'GET',
        headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        }
    }
    fetch(productEndpoint, options)
    .then(response => {
        console.log(response)
        return response.json()
    })
    .then(data => {
        console.log(data)
        productDiv.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    })
    .catch(err => {
        console.log(err)
    })
}
