import firebase_admin

cred = firebase_admin.credentials.Certificate(
    'config/firebase-adminsdk.json'
    )
firebase_app = firebase_admin.initialize_app(cred)
