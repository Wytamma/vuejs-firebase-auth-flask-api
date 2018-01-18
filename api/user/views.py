from flask import Blueprint, jsonify, request, current_app
from .auth import confirm_token, generate_confirmation_token, valid_password, firebase
from core.utils import email
from firebase_admin.auth import AuthError

user_blueprint = Blueprint('user', __name__,)


@user_blueprint.route('/signup/<email_address>')
def signup(email_address):
    """Sends signup link to email address provided"""

    # check if email exists and return
    if firebase.get_user_by_email(email_address):
        return jsonify(
            {'message': 'Account already exists with that email.'}
            ), 400

    token = generate_confirmation_token(email_address)
    url = f'{current_app.config["WEBAPP_BASE_URL"]}/auth/set-password?token={token}'

    # Email is run as a task by zappa i.e. in a new lambda instance
    email(email_address,
          subject='Sign Up to vuejs-firebase-auth-flask-api',
          body=f'Click this link to sign up.\n\n{url}')
    return jsonify(
        {'message': f'Spawned task to send signup Email to {email_address}'})


@user_blueprint.route('/set_password', methods=['POST'])
def set_password():
    data = request.get_json()
    token = data['token']
    email_address = confirm_token(token)
    if not email_address:
        return jsonify(
            {'message': 'Invaild token.'}
            ), 400  # web app should redirect to login
    # create user firebase
    password = data['password']
    if not valid_password(password):
        return jsonify({'message': 'Invaild password.'}), 400
    try:
        user = firebase.create_user(email=email_address, password=password)
    except AuthError:
        # this could be a server error or duplicate account
        return jsonify(
            {'message': "Account creation failed."}), 400

    user_token = (firebase.create_custom_token(user.uid)).decode()
    return jsonify(
        {
            'message': f'Email {email_address} confirmed. Account Created.',
            'token': str(user_token)
        }), 200  # webapp should direct to dashboard (signInWithCustomToken)
