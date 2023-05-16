function sendMail(contactForm){
    emailjs.send("service_eq1uv2d","template_2e9pylo", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
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