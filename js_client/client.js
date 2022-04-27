// to run this html head to this directory and:
// python -m http.server 8111 


const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const contentContainer = document.getElementById('content-container')
const baseEndpoint = 'http://localhost:8000/api'

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    searchForm.addEventListener('submit', handleSearch)
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
        let content = 'You are logged in!'
        handleAuthData(authData, writeContent, content)
    })
    .catch(err => {
        console.log(err)
    })
}

function handleSearch(event) {

    event.preventDefault()
    let searchFormData = new FormData(searchForm)
    let searchData = Object.fromEntries(searchFormData)
    let searchParams = new URLSearchParams(searchData)

    const searchEndpoint = `${baseEndpoint}/search/?${searchParams}`

    const options = {
        method: "GET",
        headers: {
            "content-type": "application/json",
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        },
    }

    fetch(searchEndpoint, options)
    .then(response => {
        return response.json()
    })
    .then(data => {
        writeContent(data)
    })
    .catch(err => {
        console.log(err)
    })
}

function handleAuthData(authData, callback, content) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback(content)
    }
}

function writeContent(content) {
    contentContainer.innerHTML = "<pre>" + JSON.stringify(content, null, 4) + "</pre>"
}


function getProductList() {
    const productEndpoint = `${baseEndpoint}/product/`
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
        writeContent(data)
    })
    .catch(err => {
        console.log(err)
    })
}

const searchClient = algoliasearch('3L8FH99WX4', 'c14d136e0a5a3ba4b1db7bb54bbc6e82');

const search = instantsearch({
  indexName: 'Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

  instantsearch.widgets.hits({
    container: '#hits',
  })
]);

search.start();

