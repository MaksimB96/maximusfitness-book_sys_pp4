# Maximus Fitness Booking System

(Developer: Maksims Buraks)

![Mockup image](docs/am-i-responsive.png)

[live web-page](https://maksimb96.github.io/LoveBody/)

## Table of contents

- [Maximus Fitness Booking System](#maximus-fitness-booking-system)
  - [Table of contents](#table-of-contents)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
      - [First-time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Site Owner](#site-owner)
  - [Design](#design)
    - [Design Choices](#design-choices)
    - [Kanban-Board](#kanban-board)
    - [Colour](#colour)
    - [Fonts](#fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
  - [Tech Used](#tech-used)
    - [Languages](#languages)
    - [Tools](#tools)
  - [Features](#features)
    - [Logo and Nav-Bar](#logo-and-nav-bar)
    - [](#)
    - [Index](#index)
    - [Contact Form](#contact-form)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
    - [JS Validation](#js-validation)
    - [Accessability](#accessability)
    - [Performance](#performance)
    - [Tests](#tests)
      - [Devices tested on on:](#devices-tested-on-on)
      - [Browser tested on on:](#browser-tested-on-on)
    - [Testing User Stories](#testing-user-stories)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Future Features](#future-features)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

    -Finding a site that provides ability to book a one on one session
    -To Create Bookings
    -To Update Bookings
    -To Delete Bookings
    -To Manage Bookings
    -To Create Account

### Site Owner Goals

    -Provide a simple and clean approach to booking sessions
    -Provide an area to get in contact
    -To manage and confirm bookings

## User Experience

### Target Audience

    -People looking to book a session

### User Requirements and Expectations

    -A simple and natural way to navigate the website
    -Quick acessibility to relevant information
    -Appealing design that responds accordingly
    -A simple way to get in contact/book etc.
    -Accessibility

### User Stories

#### First-time User

1. As a first time user, I want to book a session
2. As a first time user, I want easy intuative navigation
3. As a first time user, I want information presented in one location
4. As a first time user, I want to get in contact for more info

#### Returning User

5. As a returning user I want to sign back in 
6. As a returning user I want to update bookings
7. As a returning user I want to view bookings
8. As a returning user I want to delete bookings

#### Site Owner

9. As a site owner I want people to locate relevant information to booking
10. As a site owner I want people easily book and manage sessions
11. As a site owner I want the ability to update or confirm bookings

## Design

### Design Choices

Website design took into consideration company colors and elements. The website follows a clean and minimal design in order to make readability and accesability easy. Which follows the motto of minimal fitness. A clean layout with relevant information.


### Kanban-Board

A kanban board was utilised to sub divide each story into an epic (3 in total) This helped spped development up with clear cut goals
![Kanban]()
### Colour

Color choices for this project again were based solely on the company colors, being red/black/white with different shades  of grey to help accent element.

<br>

![Color Scheme](docs/features/kanban.png)

### Fonts

Montserrat, with a fall-back of sans-serif was used along with "Source Sans Pro", with the sans-serif fall-back. These were chosen because they evoke a modern and clean look, along with complementing geometry!

### Structure

The Structure of the website is a clean and minimal approach as the main focus of the website is the Crud Functionality Therefore the index page allows for ease of access to all relevant info. The nav bar is clean and simple with all elements being clear and intuative. The Index is the most animated, as the goal is to draw in people and be more welcoming. Clean design maintained throughout.

<br>

The website is made up of 8 pages:

    -The User authenticated segments 
    -The Index
    -The CRUD Functions

### Wireframes

<details><summary>Home</summary><img src="docs/wireframes/index.png"></details>

<details><summary>Book</summary><img src="docs/wireframes/book-session.png"></details>

<details><summary>Manage</summary><img src="docs/wireframes/manage.png"></details>

<details><summary>Update/Delete</summary><img src="docs/wireframes/update:delete.png"></details>

Core functionality and views remain the same throughout. Sign in/login pages are custom 

-Tablet view is exactly the same as desktop!

## Tech Used

### Languages

    -HTML
    -CSS
    -Java Script
    -Pyhton
    -Django
    

### Tools

    -Git
    -Git Hub
    -Git Pod
    -Balsamiq
    -Google Fonts
    -Adobe Color Wheel
    -Font Awesome
    -Favicon.io
    -Circle Crop
    -EmailJs
    -postgresql
    -psycopg
    -Canva
    -Boot strap 4
    -ScrollReveal function
    -pixelr
    -Django
    -SummerNote
    -Crispy Forms

## Features



### Logo and Nav-Bar

    -featured on all three pages
    -Options changed based on user authentication
    -Nav bar is fully responsive and changes to a burger style on mobile devices. Nav bar links to all relevant pages allowing for quick access.
    -Subtle animation for selected
    -Pages 2/3 have a slight difference in appearance but over all same design in order to not disrupt immersion.-
    relevant links lead to full Crud

    
![Logo & Navbar](docs/features/nav-user.png)

<br>

![Logo & Navbar](docs/features/nav-new.png)

<br>

![Logo & Navbar](docs/features/nav-burger-show.png)

![Logo & Navbar](docs/features/nav-burger.png)


### 

    -footer conistent on all pages with hover effect in order to provide clear feedback on selection
    
![Footer and Selection](docs/features/footer.png)
![Footer and Selection](docs/features/footer-select.png)



### Index

    -Clear UI
    -Responsive
    -Scroll reveal adds dynamic element to page
    -message handeling
   

![Index Segment](docs/features/scrollreveal().png)


### Contact Form

    -Allows users to leave feedback for general queries and concerns
    -Form validates email and name (full name and proper email)
    -Form Sends back email to me as soon as user leaves feedback
    -Clear feedback

![Contact-form](docs/features/contact-form.png)

<br>

![Contact-form](docs/features/contact-segment.png)



## Validation

### HTML Validation
W3C mark-up was utilised in order to validate html of the website. All Pages pass with no errors. Warnings are related to various segments not using Headings, but utilise div elements.

<details><summary>Index</summary>
<img src="docs/validations/index-valid.png">
</details>

<details><summary>login</summary>
<img src="docs/validations/login-valid.png">
</details>

<details><summary>logout</summary>
<img src="docs/validations/logout-valid.png">
</details>

<details><summary>Manage</summary>
<img src="docs/validations/manage-valifd-html.png">
</details>

<details><summary>Sign-Up</summary>
<img src="docs/validations/sign-up-valid.png">
</details>

<details><summary>Delete</summary>
<img src="docs/validations/delete-valid-html.png">
</details>



<br>

### CSS Validation
W3C CSS validator was utilised in order to make sure the css code passes standards with no errors.

<details><summary>Full Document</summary>
<img src="docs/validation/css-valid.png">
</details>

<br>

### Python Validation

CI Python linter used here

<details><summary>Forms</summary>
<img src="docs/validation/forms-py.png">
</details>

<details><summary>Model</summary>
<img src="docs/validation/models-py.png">
</details>


<details><summary>View</summary>
<img src="docs/validation/views-py.png">
</details>

### JS Validation
JSHint validator was utilised in order to make sure the javascript code passes standards with no errors or warnings, All functions marked as "unused" are called on click in HTML code segments, images of relevnt code is attached to validations.

<details><summary>Email Js And Script</summary>
<img src="docs/validations/script.png">
<img src="docs/validations/sendEmail..png">
</details>

<br>

### Accessability
Wave WebAIM was utilized in order to make sure the website met high accessability standards. All pages pass with no errors or contrast errors. Warnings are due to things such as logo having the same link as the hom, which is an intentional feature. The form segment states the labels are not owned by input eventhough they have been propeerly attributed.

<details><summary>Index</summary>
<img src="docs/validations/indexwave.png">
</details>
<details><summary>Fitness Quiz</summary>
<img src="docs/validations/quizwave.png">
</details>
<details><summary>Feedback</summary>
<img src="docs/validations/feedbackwave.png">
</details>

<br>

### Performance
Google light house was used in order to confirm good standards of performace

<details><summary>Index</summary>
<img src="docs/validations/index-perform.png">
</details>
<details><summary>Fitness Quiz</summary>
<img src="docs/validations/fitquiz-perform.png">
</details>
<details><summary>Feedback</summary>
<img src="docs/validations/form-perform.png">
</details>

<br>

### Tests

#### Devices tested on on:
    -Iphone SE, XR, 11, 12, 13
    -Ipad
    -Macbook Pro/Air
    -Lenovo Platform
    -Dell Platform

#### Browser tested on on:
    -Chrome
    -Mozilla
    -Safari
    -Brave/Brave Mobile

### Testing User Stories

1. As a first time user, I want to test my fitness knowledge

2. As a first time user, I want to test my nutrition knowledge

5. As a returning user I want to refresh my knowledge on fitness

6. As a returning user I want to refresh my knowledge on nutrition

7. As a returning user I want to see additional questions added

3. As a first time user, I want information presented in one location

4. As a first time user, I want to leave feedback for further addition of questions

9. As a site owner I want people to locate relevant information to the quiz

10. As a site owner I want people to be able to play as many times

11. As a site owner I want individuals to get in contact


<br>

| **Feature** | **Action** | **Expected Results** | **Final Result** |
|-------------|------------|----------------------|------------------|
|             |            |                      |                  |
| Home page, Linked Icons| Burger Menu/ Desktop menu show relevant info, icons link to poi's| Interactive Elements prompt to trravel to relevant poi's| Home page prompts user to travel to all locations from home page|
|Quiz| Allows user to test knowledge in relation to fitness| Clear visual indicators for correct/wrong answer, questions cycle and then reset as intended|Quiz Works as intended|
|Feedback Form| Input fields only submit once form validated| Form validates inputs and sends feedback to me| Form Works as intended|

<details><summary>Screenshot</summary>
<img src="docs/testing-features/index-uf.jpg">
<img src="docs/testing-features/quizuf-1.jpg">
<img src="docs/testing-features/quizuf2.jpg">
<img src="docs/testing-features/quizuf3.jpg">
<img src="docs/testing-features/formuf.jpg">
</details>
<br>



8. As a returning user I want to be able to locate relevant social links

| **Feature** | **Action** | **Expected Results** | **Final Result** |
|-------------|------------|----------------------|------------------|
|             |            |                      |                  |
|Social Media Links|User has access socials| Functional links| Works as intended|
<details><summary>Screenshot</summary>
<img src="docs/testing-features/socialsuf.jpg">
</details>
<br>


## Bugs

| **Bug** | **Fix** | 
|---------|---------|
|         |         | 
|Restart Scores did not work as intended| Created new button instead of changing inner html and defind it, and added functions that reset score on click via event listener|
|Form not validating|Added correct string in order validate |
|Initial break of quiz| Corrected elements by id and programmed restart button and function correctly|

## Deployment

Deployment of site was acheived through these steps:
1. I navigated to the settings section on git hub repositories on my repository.
2. I then selected the pages link on the left side.
3. I then selected source for the branch prompt.
4. Roughly, 2 minutes after refreshing I recieved a link to my site: https://maksimb96.github.io/LoveBody/ 

## Future Features

There are a few more feartures that I would like to implement in the future. These Include:
1.Polished Nav Bar with smooth transition
2.Timer function to quiz
3.Randomize the order of how button answers display
4.A progress Bar to track progress

## Credits

### Media

All media created by me using  <a href="https://www.canva.com/">Canva</a>, this includes Icons and backgound images.
<br>
Any Icons used found on <a href="https://fontawesome.com/">Font Awesome</a>
<br>
Burger Image by <a href="https://www.flaticon.com/free-icon/menu_4254068?term=menu-burger&page=1&position=2&page=1&position=2&related_id=4254068&origin=tag#">Andy Horvath</a>
<br>
X Image by <a href="https://www.flaticon.com/free-icon/close_2997911?term=x&page=1&position=5&page=1&position=5&related_id=2997911&origin=tag# ">Fuzzee</a>
    
### Code 

1. 404 page code provided by Mo Shami_mentor from code institue
2. favicon idea provided by Mo Shami_mentor, site used found <a href="https://favicon.io/"> here</a>
3. Form Validation inspiraation by <a href="https://www.youtube.com/watch?v=fz8bwvn9lA4"> Easy Tutorials</a>
4. Increment of answers inspired by LoveMaths by Code Institute
5. Text shadow property taken from <a href="https://www.w3schools.com/cssref/css3_pr_text-shadow.php"> w3schools</a>
6. Email Validation strings by <a href="https://www.w3resource.com/javascript/form/email-validation.php">W3Schools</a>
7. Burger Nav bar help from tutor support
8. Reset button functionality help from tutor support
9. EmailJs instructions may be found on <a href="https://www.emailjs.com/">EmailJS</a>
10. Quiz inspiration taken from  <a href="https://www.youtube.com/watch?v=riDzcEQbX6k">Web Dev Simplified</a>


## Acknowledgements

-I would like to thank Victor my mentor
<br>
-CI for provide me the knowledge to under-take this task
<br>
-Tutor Support for provideing better knowledge to implement the code!
<br>
-My beautiful girlfriend who almost got all my typos and My friend for design related advice
<br>
-The wonderful community over on Slack!












