

class Header():

    def __init__(self, alg, typ):
        
        self.alg = alg
        self.typ = typ


class Payload():

    def __init__(self, iss, exp, sub, aud, claims):

        self.iss = iss
        self.exp = exp
        self.sub = sub
        self.aud = aud
        self.claims = claims


class Signature():

    def __init__(self, signature_string):
        
        self.signature_string = signature_string


class SD_JWT():

    def __init__(self, header, payload, signature):
        
        self.header = header
        self.payload = payload
        self.signature = signature

header = Header("HS256", "JWT")
payload = Payload(12,13,"Dani","Lumi", [])
signature = Signature("jknsfvnvdvn4gnir5")
sdjwt = SD_JWT(header, payload, signature)
