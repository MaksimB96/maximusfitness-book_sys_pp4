function sendMail(contactForm){
    emailjs.send("gmail", "template_2e9pylo", {
        "from_name": contactForm.name.value,
        "form_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("Success", response)
        },
        function(error){
            console.log("Error", error)
        })
}