import sdjwt
import token_settings as settings
from time import time, ctime
import base64



def encode_base64(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def encode64_header(header):
    alg_str = "alg:" + str(header.alg)
    typ_str = "typ:" + str(header.typ)
    header_str = alg_str + typ_str
    return encode_base64(header_str)

def encode64_payload(payload):
    iss_str = "iss:" + str(payload.iss)
    exp_str = "exp:" + str(payload.exp)
    sub_str = "sub:" + str(payload.sub)
    aud_str = "aud:" + str(payload.aud)
    claims_str = str(payload.claims).replace(' ', '').replace(',', '').replace('{', '').replace('}', '').replace("'", '')
    payload_str = iss_str + exp_str + sub_str + aud_str + claims_str
    return encode_base64(payload_str)


def create_signature(enc_header, enc_payload):
    pass

def build_SDJWT():
    pass
    

def parse_data_to_SDJWT(filepath):
    t = time()
    claims_dic = dict()

    with open(filepath) as file:
        for line in file:
            claim = line.split(":")
            claim[1] = claim[1].strip()
            claims_dic[claim[0]] = claim[1]

    header = sdjwt.Header(settings.alg, settings.typ)
    payload = sdjwt.Payload(ctime(t), 12345678, settings.sub, settings.aud, claims_dic)

    enc_header = encode64_header(header)
    enc_payload = encode64_payload(payload)
    signature = create_signature(enc_header, enc_payload)
    draft_sdjwt = sdjwt.SD_JWT(enc_header, enc_payload, signature)
    sd_jwt = build_SDJWT(draft_sdjwt)

    return sd_jwt
       



def parse_SDJWT_to_JSON(sd_jwt):
    pass

parse_data_to_SDJWT("data/text/sample1.txt")

dict1 = {'one':1, 'two':2}
str1 = str(dict1)
str2 = str1.replace(' ', '').replace(',', '').replace('{', '').replace('}', '').replace("'", '')
print(str2)