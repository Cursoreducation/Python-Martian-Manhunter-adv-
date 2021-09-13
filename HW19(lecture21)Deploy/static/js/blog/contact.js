let contactButton = document.getElementById('sendContactForm');
contactButton.addEventListener('click', function (e) {
    e.preventDefault();

    let data = {
         title: document.getElementById('title').value,
         email: document.getElementById('email').value,
         description: document.getElementById('description').value,
    }
    fetch("/api/contact", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => {
        if (response.status == 200) {
            alert("Message sent to our support team!");
        } else {
            alert("Something went wrong! Our team working on!");
        }
    })
})