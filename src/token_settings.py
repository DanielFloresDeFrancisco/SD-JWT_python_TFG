# General settings for inmutable claims of a SD-JWT
from time import time, ctime
# HEADER
alg = "HS256"
typ = "JWT"

# PAYLOAD
aud = "Javier"
sub = "Daniel"

t = time()
tiempo = ctime(t)
print(tiempo)