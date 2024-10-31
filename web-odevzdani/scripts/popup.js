let modal = document.getElementById('submit')


function openPopup(){
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('comment').value;
    var output = document.getElementById('output');

    modal.classList.add('modal-open');

    if (name.trim() !== '' && message.trim() !== '') {
        output.textContent = "Thank you!\nWe will contact you on the subject: " + subject + " here: " + email + "soon\n";
    } else {
        output.textContent = "Please fill in both name and message fields.";
    }
};

function closePopup(){
    modal.classList.remove('modal-open')
};