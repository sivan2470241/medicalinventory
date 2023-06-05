from django.utils.crypto import salted_hmac
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def generate_token(registration):
    token = salted_hmac("registration_token", urlsafe_base64_encode(force_bytes(user.pk))).hexdigest()
    return token