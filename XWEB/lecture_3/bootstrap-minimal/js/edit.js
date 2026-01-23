
function open_dialog(dialogId) {
    const dialog = document.getElementById(dialogId);
    if (dialog && typeof dialog.showModal === 'function') {

        setTimeout(() => {
            if (dialog.open) {
                dialog.close();
            }
        }, 10000); 
        dialog.showModal();
    } else {
        console.error(`Dialog s ID ${dialogId} nebyl nalezen.`);
    }
}


function close_dialog(dialogId) {
    const dialog = document.getElementById(dialogId);
    if (dialog && typeof dialog.showModal === 'function') {
        dialog.close();
    } else {
        console.error(`Dialog s ID ${dialogId} nebyl nalezen.`);
    }
}

function showNotification(message) {
    // Bere to element s class alert a změní to jeho styl, který je původně nějak nastaven a nejde vidět
    // notifikace jako akce po úspěšném uložení
    const notification = document.getElementById('save_notification');
    notification.textContent = message;
    if (notification) {
        console.log('Zobrazena notifikace:', message);
        notification.style.display = 'block';
        // setTimeout(() => {
        //     notification.style.display = 'none';
        // }, 5000); // Schová notifikaci po 5 sekundách
    }
}

function confirm_edit(confirmButtonId, formId, dialogId) {
    const form = document.getElementById(formId);
    const button = document.getElementById(confirmButtonId);

    button.addEventListener('click', function() {
        
        close_dialog(dialogId);
        // čtení z formuláře musí být ve chvíli aktualizace.
        const formData = new FormData(form);
        formData.append('save_update', 'true');    // přidání informace, která mi řídí logiku na serveru

        fetch(form.action, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                // zobrazení notifikace p nějakou dobu, pak reload, abych byl zas na /users
                showNotification('Uživatel byl úspěšně upraven.');
                setTimeout(() => {
                    window.location.reload();
                }, 5000);
            } else {
                console.error('Chyba při odesílání formuláře.');
            }
        })
        .catch(error => {
            console.error('Chyba při odesílání formuláře:', error);
        });
    });

}

function confirm_delete(confirmButtonId, dialogId) {
    const button = document.getElementById(confirmButtonId);
    
    button.addEventListener('click', () => {
        const emailToDelete = button.getAttribute('data-email');
        // na pozadí posílám request (tady POST) na tuto adresu. To mi zpracovává router a na FE zůstává stejná stránka
        fetch(`/users/delete/${encodeURIComponent(emailToDelete)}`, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (response.ok) {
                close_dialog(dialogId);
                // showNotification('Uživatel byl úspěšně smazán.');
                // setTimeout(() => {
                //     window.location.reload();
                // }, 5000);
            }
            else {
                console.error('Chyba při mazání uživatele.');
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete_button');
    const saveEdit = document.getElementById('edit_form');
    const cancelButton = document.getElementById('edit_no');
    const cancelDeleteButton = document.getElementById('delete_no');
    const dialogIdCile = 'confirm_edit';
    const dialogDelete = 'ask_delete';
    const confirmButton = document.getElementById('confirm_edit_btn');
    const confirmDeleteButton = document.getElementById('confirm_delete_btn');

    deleteButtons.forEach(button => {

        if (button) {
            button.addEventListener('click', (event) => {
                event.preventDefault();    // zabrání redirectu na /users/delete/...
                const email = button.getAttribute('data-email');
                confirmDeleteButton.setAttribute('data-email', email);
                open_dialog(dialogDelete);
            });
        }
    });

    if (saveEdit) {
        saveEdit.addEventListener('submit', function(event) {
            event.preventDefault();
            event.stopPropagation();
            open_dialog(dialogIdCile);
        });
    }
    if (cancelButton) {
        cancelButton.addEventListener('click', () => {
            close_dialog(dialogIdCile);
        });
    }

    if (cancelDeleteButton) {
        cancelDeleteButton.addEventListener('click', () => {
            close_dialog(dialogDelete);
        });
    }

    if (confirmButton && saveEdit) {
        confirm_edit('confirm_edit_btn', 'edit_form', dialogIdCile);
    }
    if (confirmDeleteButton) {
        
        confirm_delete('confirm_delete_btn', dialogDelete);
    };
});