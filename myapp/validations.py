from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def custom_validation(data):
    email = data.get('email').strip()
    username = data.get('username').strip()
    password = data.get('password').strip()
    ##
    if UserModel.objects.filter(email=email).exists():
        message = 'An account with this email already exists!'
        return message
    ##
    if not password or len(password) < 8:

        return 'choose another password, min 8 characters'

    ##
    if not username:
        return 'choose another username'

    return True


def validate_email(data):

    email = data['email'].strip()
    if not email:
        return False
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        return False
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        return False
    return True