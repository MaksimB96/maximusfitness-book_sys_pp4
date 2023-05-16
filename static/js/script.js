// Pre-Loader
var loader = document.getElementById("preloader");

window.addEventListener("load", function () {
    loader.style.display = "none";
});


/**
 * This function validates contact form on index
 */

function validation(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("text_area").value;
    var error_message = document.getElementById("error_message");
    var text;

    if(name.length < 5){
        text = "Please Enter a valid name";
        error_message.innerHTML = text;
        return false;
    }

    if(email.indexOf("@") == -1 || email.length < 6){
        text = "Please Enter A Valid Email";
        error_message.innerHTML = text;
        return false;
    }

    if(message.length <= 50){
        text = "Please Enter A Valid Message Above 50 Characters";
        error_message.innerHTML = text;
        return false;
    }

    return true;
}


/**
 * Scroll reveal utilizes npm to create on scroll interactivity
 */

// Nav-Logo
ScrollReveal().reveal('.navbar-brand', {
    duration: 2000,
    origin: 'bottom'
});

// About Section - Index
ScrollReveal().reveal('.left-slide-text', {
    duration: 2000,
    origin: 'bottom',
    distance: '300px'
});

ScrollReveal().reveal('.right-slide-img', {
    duration: 2000,
    origin: 'bottom',
    distance: '300px'
});

ScrollReveal().reveal('.location', {
    duration: 2000,
    origin: 'left',
    distance: '300px'
});

ScrollReveal().reveal('.right-slide-text', {
    duration: 2000,
    origin: 'right',
    distance: '300px'
});

// Carousel - Index
ScrollReveal().reveal('.tester_new', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    delay: 1000
});

// Contact us - Index
ScrollReveal().reveal('.con-name', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
});

ScrollReveal().reveal('.con-email', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    delay: 250
});

ScrollReveal().reveal('.con-text', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    delay: 500
});

ScrollReveal().reveal('.con-submit', {
    duration: 2000,
    origin: 'left',
    distance: '300px',
    delay: 750
});

ScrollReveal().reveal('.map-area', {
    duration: 2000,
    origin: 'right',
    distance: '300px',
});

/**
 * Timeout finction dismisses alert
 */

setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);