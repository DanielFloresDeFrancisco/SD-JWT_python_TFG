import os
import base64
# General settings for inmutable claims of a SD-JWT
from time import time, ctime
# HEADER
alg = '"HS256"'
typ = '"JWT"'

# PAYLOAD
aud = '"Verifier"'
sub = '"Holder"'


def generate_random256_bit_key():
    random_key = os.urandom(32)
    base64url_key = base64.urlsafe_b64encode(random_key).rstrip(b'=').decode('ascii')   
    return base64url_key