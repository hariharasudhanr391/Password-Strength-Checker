document.getElementById('password').addEventListener('input', function() {
    var password = this.value;

    fetch('/check_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        var strengthMessage = document.getElementById('strengthMessage');
        var strengthBar = document.getElementById('strengthBar');

        strengthMessage.textContent = data.message;
        strengthBar.className = data.className;
    });
});
