// to run this html head to this directory and:
// python -m http.server 8111 


const loginForm = document.getElementById('login-form')
const baseEndpoint = 'http://localhost:8000/api'

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {

    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/auth/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    const options = {
        method: 'POST',
        headers: {
            'ContentType': 'application/json'
        },
        body: bodyStr
    }
    console.log(bodyStr)
    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response)
        return response.json()
    })
    .then(data => {
        console.log(data)
    })

}