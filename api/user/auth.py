from itsdangerous import URLSafeTimedSerializer
from flask import current_app

import firebase_admin
from firebase_admin import credentials
from firebase_admin.auth import AuthError


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email


def valid_password(password):
    if len(password) < 8:
        return False
    return True


cred = credentials.Certificate(
    'config/firebase-adminsdk.json'
    )
firebase_app = firebase_admin.initialize_app(cred)


class firebase:
    def create_user(email, password, email_verified=True):
        user = firebase_admin.auth.create_user(
            email=email,
            password=password,
            email_verified=email_verified,
            app=firebase_app)
        return user

    def get_user_with_uid(uid):
        try:
            user = firebase_admin.auth.get_user(uid, app=firebase_app)
        except AuthError:
            # user ID does not exist.
            return None
        except ValueError:
            # If the user ID is None, empty or malformed.
            return None
        return user

    def get_user_by_email(email):
        try:
            user = firebase_admin.auth.get_user_by_email(email, app=firebase_app)
        except AuthError:
            # user email does not exist.
            return None
        except ValueError:
            # If the email is None, empty or malformed.
            return None
        return user

    def create_custom_token(uid, developer_claims=None):
        token = firebase_admin.auth.create_custom_token(
            uid, developer_claims=None, app=None
            )
        return token
