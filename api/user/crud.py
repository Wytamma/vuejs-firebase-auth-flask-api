from firebase_admin.auth import AuthError
import firebase_admin
from core.firebase import firebase_app


def create_user(email, password, email_verified=True):
    user = firebase_admin.auth.create_user(
        email=email,
        password=password,
        email_verified=email_verified,
        app=firebase_app
    )
    return user


def get_user_with_uid(uid):
    try:
        user = firebase_admin.auth.get_user(
            uid,
            app=firebase_app
        )
    except AuthError:
        # user ID does not exist.
        return None
    except ValueError:
        # If the user ID is None, empty or malformed.
        return None
    return user


def get_user_by_email(email):
    try:
        user = firebase_admin.auth.get_user_by_email(
            email,
            app=firebase_app
        )
    except AuthError:
        # user email does not exist.
        return None
    except ValueError:
        # If the email is None, empty or malformed.
        return None
    return user


def create_custom_token(uid, developer_claims=None):
    token = firebase_admin.auth.create_custom_token(
        uid,
        developer_claims=developer_claims,
        app=firebase_app
    )
    return token