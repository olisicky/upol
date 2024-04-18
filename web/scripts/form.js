// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];



document.getElementById('submit').addEventListener('click', function() {

    var name = document.getElementById('name').value;
    var name = document.getElementById('email').value;
    var name = document.getElementById('subject').value;
    var message = document.getElementById('comment').value;
    var output = document.getElementById('output');
    
    // Check if both name and message are filled
    if (name.trim() !== '' && message.trim() !== '') {
        output.textContent = "Name: " + name + "\nMessage: " + message;
    } else {
        output.textContent = "Please fill in both name and message fields.";
    }
});


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};