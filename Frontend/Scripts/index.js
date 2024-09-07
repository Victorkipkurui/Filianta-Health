function postData(url, data) {
    fetch('http://127.0.0.1:8000/login/', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(data), 
    })
    .then(response => response.json()) 
    .then(data => {
        console.log('Success:', data); 
    })
    .catch((error) => {
        console.error('Error:', error); 
    });
}

document.getElementsByClassName('js-signup').addEventListener('click', () => {
    sign_up();
});

document.getElementsByClassName('js-login').addEventListener('click', function() {
    window.location.href = '/login/';
});