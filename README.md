# videssy

A website where you can upload and watch videos, subscribe to channels and comment on their videos. This website is supposed to be a YouTube clone. The frontend uses tailwind and isn't meant to be flashy or well-designed. The backend code is what's to be shown as portfolio code.

License: MIT

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. 

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Starting Development server

-   To install dependencies, use either of the following two commands(make sure pipenv is installed):

        $ pipenv sync
        OR 
        $ pipenv install -r requirements.txt

-   To start a **development server**, use this command:

        $ python manage.py runserver

You may view the page on http://127.0.0.1:8000

## Deployment

This project is not intended for deployment and only serves as part of my portfolio. If you do intend to use it for deployment, do it at your own discretion.
