function showNotification(message) {
    // Bere to element s class alert a změní to jeho styl, který je původně nějak nastaven a nejde vidět
    // notifikace jako akce po úspěšném uložení
    const notification = document.getElementById('login_notification');
    notification.textContent = message;
    if (notification) {
        console.log('Zobrazena notifikace:', message);
        notification.style.display = 'block';
        setTimeout(() => {
            notification.style.display = 'none';
        }, 5000);
    }
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.getElementById('login_button');

    if (loginButton) {
        loginButton.addEventListener('click', (event) => {
            // zde můžete přidat vlastní validační logiku
            const username = document.querySelector('input[name="user"]').value;
            const password = document.querySelector('input[name="psw"]').value;

            if (username === '' || password === '') {
                event.preventDefault();
                showNotification('Prosím, vyplňte všechny povinné údaje.');
            }

            if (!isValidEmail(username)) {
                event.preventDefault();
                showNotification('Prosím, zadejte platnou e-mailovou adresu jako uživatelské jméno.');
            }

            fetch('/login/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user: username, psw: password })
            })
        });
    }
});
