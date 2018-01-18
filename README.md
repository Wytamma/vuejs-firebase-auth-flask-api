# vuejs-firebase-auth-flask-api
I extended Anas Mammeri's vue.js/firebase tutorial [Vue 2 + Firebase: How to build a Vue app with Firebase authentication system in 15 minutes](https://medium.com/@anas.mammeri/vue-2-firebase-how-to-build-a-vue-app-with-firebase-authentication-system-in-15-minutes-fdce6f289c3c) to include a flask backend. clone this repo to get new ideas off the ground quicker.

## setup /api
Replace missing configs:
 - api/config add `_passwords.py` (server email details)
 - api/config add `firebase-adminsdk.json` (firebase-sdk-file)

Commands:
 - `pipenv install` (install dependancies)
 - `export FLASK_APP=app.py`
 - `flask run` (start server)

## setup /webapp
Replace missing configs:
 - webapp/config add `firebase.config.json` (firebase-sdk-file)

Commands:
 - `npm install` (install dependancies)
 - `npm run dev` (serve with hot reload at localhost:8080)
 - `npm run build` (build for production with minification)

## basics
when you load localhost:8080 you'll be directed to a login page. click the link to create a new account. i made a design choice here... firebase won't verify email before you create an account. I use the flask backend to do email verification before account creation. enter details, get link, set password, login.

## production
the idea is that the backend will be run on aws lambda using zappa and the frontend build will be hosted on was s3. this is about the cheapest option.

> Written with [StackEdit](https://stackedit.io/).
