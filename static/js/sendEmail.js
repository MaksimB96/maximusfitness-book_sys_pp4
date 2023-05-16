function sendEmail(){

    const templateParams = {
        "from_name": document.getElementById("name").value,
        "from_email": document.getElementById("email").value,
        "message": document.getElementById("text_area").value
    };

    emailjs.send("service_eq1uv2d","template_2e9pylo", templateParams)
    .then(
        function(response) {
            console.log("Success", response);
        },
        function(error){
            console.log("Error", error);
        });
}