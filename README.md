# Art By Heart Sketch

Art By Heart Sketch is a website designed for users to view artwork made by the website owner and commisson the owner to draw custom pieces for themselves.

# Motivation

I decided to build this website for my sister who sells her artwork through Instagram, Facebook and Twitter but does not have an easy way to demonstrate her artwork and get buyers specification. The Website fulfils this need and allows her to easily upload her work and find new potential contacts and buyers.   

# Table of contents
1. [Project Description](#project-description)
    1. [Navigation](#navigation)
    2. [Landing Page](#landing-page)
    3. [My Profile](#my-profile)
    4. [Sign Up](#sign-up)
    5. [Log Out](#log-out)
    6. [All Products](#all-products)
    7. [Games](#games)
    8. [Consoles](#consoles)
    9. [Accessories](#accessories)
    10. [Check Out](#check-out)
    11. [Responsive Design](#responsive-design)
2. [Technologies Used](#technologies-used)
3. [Development](#development)
4. [Deployment](#deployment)
5. [Tests](#tests)
6. [Validators](#validators)
7. [Bugs & Solutions](#bugs-&-solutions)
8. [Updates](#updates)
9. [Credits](#credits)


## Project Description <a name="project-description"></a>
Art By Heart Sketch is desigend to give the user an example of what kinds of art they can commission from the artist and easily send the artist an email to commission the type of drawing they want. The website uses Python, Django Full Stack Framework, Bootstraps and Cloudinary for static files and image storage.  

<hr>

- Navigation <a name="navigation"></a>


- Landing Page <a name="landing-page"></a>

    The landing page is a read only page that demostrates what the user will get and the prices that the artist will charge. 


- My Profile <a name="my-profile"></a>

- Sign Up <a name="sign-up"></a>

- Log Out <a name="log-out"></a>

- All Products <a name="all-products"></a>

- Games <a name="games"></a>

- Consoles <a name="consoles"></a>

- Accessories <a name="accessories"></a>

- Check Out <a name="check-out"></a>

- Responsive Design <a name="responsive-design"></a>

    The website responds to large, medium and small screen sizes by shrinking the navbar to a burger button and displaying the 
    comment section in a single column. All elements are sized accordingly using bootstraps containers, rows and column. 

    Below are images of the responsive design as Heroku will not allow the app to connect to a "am I responsive website."


## Technologies Used <a name="technologies-used"></a>
  For this project the main technologies used were Python, Django, Bootstraps. 
  Python was used as it is required for Django and Django was used to save time when creating databases, authorization, tests, ect. 
  Cloudinary was used to store static files and images when the website is deployed on Heroku, as Heroku will delete images when the dynos are reset. 
  Bootstraps was used to enable easy editing of html and css elements so the wesite could be developed faster. 
  
  Along with the above technologies many python modules were installed, the full list can be seen below:

  - asgiref==3.5.2
  - backports.zoneinfo==0.2.1
  - boto3==1.26.21
  - botocore==1.29.21
  - dj-database-url==0.5.0
  - Django==4.1.2
  - django-allauth==0.51.0
  - django-crispy-forms==1.14.0
  - django-storages==1.13.1
  - fontawesomefree==6.2.0
  - gunicorn==20.1.0
  - jmespath==1.0.1
  - oauthlib==3.2.2
  - Pillow==9.3.0
  - psycopg2==2.9.5
  - PyJWT==2.6.0
  - python3-openid==3.2.0
  - requests-oauthlib==1.3.1
  - s3transfer==0.6.0
  - sqlparse==0.4.3
  - stripe==5.0.0
  - whitenoise==6.2.0

## Development <a name="development"></a>


## Deployment <a name="deployment"></a>
  
  The Game Hunter website was deployed on Heroku using the following steps:
  
  1.  I prepared Procfile
  2.  I created the app game-hunter on Heroku 
  3.  I navigated to the resources tab and added the Heroku postgres add on pack 
  4.  Then I connected the postgres data base url in my repository
  5.  On the Heroku website I then navigated to the deployment tab and connect my Github repository to Heroku 
  6.  I allowed automatic commits so that Heroku would always have the current version of my app 
  7.  I set up the config vars on the setting tab
  8.  Then I successfully deployed my app using the deploy branch button. 

<hr>

## Tests <a name="tests"></a>

- Unit Testing 

  Both automated and manual testing has been performed on this projects. 
  
  All automated tests can be found in the tests.py file.
  
  unittest tests simple things like urls being resolved.

  <hr> 

- Functional testing 

  Authentication

  Description: 

  Makes sure a user can sign up to the website

  Steps:

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the sign up link.
  2. Enter email(optional), username and password.
  3. Click Sign up.
  
  Expected:

  The users username is displayed in the navbar and they can comment on the gallery page.

  Actual: 

  The users username is displayed in the navbar.

  <hr>

  Description: 

  Makes sure a user can log in once they are signed up

  Steps:

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Enter username and password.
  3. Click log in.
  
  Expected:

  The user to be taken to the home page and their username to be displayed on the navbar.

  Actual: 

  The user to be taken to the home page and their username to be displayed on the navbar.

  <hr>

Description: 

  Makes sure a user can log out once they are logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log out link.
  2. The user is presented with a question asking if they are sure they wish to log out.
  3. Click the log out button. 

  Expected: 

  User is redirected to the home page and username no longer visible.

  Actual:

  User is redirected to the home page and username no longer visible.

  <hr>

  Description: 

  Upload Artwork link displayed when logged in as superuser.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in as a superuser.
  3. The superuser can now see the upload artwork link in the navbar.

  Expected: 

  Superuser is now able to see the upload artwork link in the navbar.

  Actual:

  Superuser is now able to see the upload artwork link in the navbar.

  <hr> 

   Description: 

   Upload Artwork link allows a superuser to upload new artwork with a title.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in as a superuser.
  3. The superuser can now see the upload artwork link in the navbar.
  4. Click the upload artwork link. 
  5. The superuser is taken to a new page with the title charfield and images selection field.
  6. The superuser types a title and selcts an image from thier files.
  7. Click the upload button.
  8. The superuser is then taken to the gallery page.

  Expected: 

  The title and image that the superuser has selected is displyed on the Gallery page.

  Actual:

  The title and image that the superuser has selected is displyed on the Gallery page.

  <hr>

  Description: 

  Able to see add comment link only when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user is now able to see the add comment button on the gallery page. 

  Expected: 

  User is able to see add comment link.

  Actual:

  User is able to see add comment link.

  <hr>

  Description: 

  User is able to add a comment when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user is now able to add a comment to a piece of uploaded artwork.  

  Expected: 

  User is able to add a comment.

  Actual:

  User is able to add a comment.

  <hr>

  Description: 

  User is able to update only their own comments when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user can now only update comments that they have added.   

  Expected: 

  User is able to update only their own comments.

  Actual:

  User is able to update only their own comments.

  <hr>

   Description: 

  User is able to delete only their own comments when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user can now only delete comments that they have added.   

  Expected: 

  User is able to delete only their own comments.

  Actual:

  User is able to delete only their own comments.

  <hr>

   Description: 

  User is able to fill in normal commssion form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the normal commissions form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in normal commissions form and see success message.

  Actual:

  User is able to fill in normal commissions form and see success message.

  <hr>

  Description: 

  User is able to fill in reference sheet form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the reference sheet form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in reference sheet form and see success message.

  Actual:

  User is able to fill in reference sheet form and see success message.

  <hr>

  Description: 

  User is able to fill in the custom form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the custom form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in the custom form and see success message.

  Actual:

  User is able to fill in the custom form and see success message.

  <hr>

  Description: 

  The normal commissions form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on normal commissions form appears in email inbox.

  Actual:

  All information filled in on normal commissions form appears in email inbox.

  <hr>

  Description: 

  The normal reference sheet form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on reference sheet form appears in email inbox.

  Actual:

  All information filled in on reference sheet form appears in email inbox.

  <hr>

  Description: 

  The normal custom form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on custom form appears in email inbox.

  Actual:

  All information filled in on custom form appears in email inbox.

<hr>

## Validators <a name="validators"></a>


### Lighthouse


### WC3 CSS


### WC3 HTML

<img src = 'static/images/WC3 HTML validator.png'>

<hr>

### PEP8


## Bugs & Solutions <a name="bugs-&-solutions"></a> 



## Updates <a name="updates"></a>


## Credits <a name="credits"></a>

Special thanks to Daisy McGirr for mentoring me throughout this project.







































DO NOT DELETE

background image source
https://arstechnica.com/gaming/2020/12/ars-technicas-best-games-of-2020/

removing products from bag not displaying toasts 

Webhooks not working (401 (Unauthorized))

update button on bag not working



<!-- Section: Social media -->
      <section class="mb-4">
        <!-- Facebook -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!">
          <i class="fab fa-facebook"></i>
        </a>

        <!-- Twitter -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!" rel="noopener" role="button"><i
            class="fab fa-twitter"></i></a>

        <!-- Google -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!" rel="noopener" role="button"><i
            class="fab fa-google"></i></a>

        <!-- Instagram -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!" rel="noopener" role="button"><i
            class="fab fa-instagram"></i></a>

        <!-- Linkedin -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!" rel="noopener" role="button"><i
            class="fab fa-linkedin"></i></a>

        <!-- Github -->
        <a class="btn btn-outline-light btn-floating m-1" href="#!" rel="noopener" role="button"><i
            class="fab fa-github"></i></a>
      </section>
      <!-- Section: Social media -->