import sdjwt
import token_settings as settings
from time import time, ctime
import base64
import hmac
import hashlib

def removing_whitespaces_pair_kv(input_str):
    inside_string = False
    compact_result = ""
    
    for char in input_str:
        if char == "'":  
            inside_string = not inside_string
            compact_result += '"'
        elif char in [' ', '\n', '\t'] and not inside_string:
            continue  
        else:
            compact_result += char
    return compact_result

def encode_base64url(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    base64url_string = base64_string.replace("+", "-").replace("/", "_").rstrip("=")    
    return base64url_string

def encode64_header(header):
    alg_str = '{"alg":' + header.alg + ','
    typ_str = '"typ":' + str(header.typ)
    header_str = alg_str + typ_str + '}'
    return encode_base64url(header_str)

def encode64_payload(payload):
    iss_str = '{"iss":' + str(payload.iss) + ','
    exp_str = '"exp":' + str(payload.exp) + ','
    sub_str = '"sub":' + str(payload.sub) + ','
    aud_str = '"aud":' + str(payload.aud) + ','
    draft_claims = removing_whitespaces_pair_kv(str(payload.claims))
    claims_str = draft_claims.replace("'", '"').replace('{', '').replace('}', '')
    payload_str = iss_str + exp_str + sub_str + aud_str + claims_str + '}'
    return encode_base64url(payload_str)

def create_signature(enc_header, enc_payload):
    to_be_signed = enc_header + '.' + enc_payload
    secret_key = settings.generate_random256_bit_key()
    print("Secret:", secret_key)
    signature = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=to_be_signed.encode('utf-8'),  
        digestmod=hashlib.sha256  
    ).digest()
      
    signature_base64url = base64.urlsafe_b64encode(signature).rstrip(b'=').decode('utf-8')
    
    return signature_base64url

def build_SDJWT(draft_sdjwt):
    return draft_sdjwt.header + '.' + draft_sdjwt.payload + '.' + draft_sdjwt.signature
    
def parse_data_to_SDJWT(filepath):
    t = time()
    claims_dic = dict()

    with open(filepath) as file:
        for line in file:
            claim = line.split(":")
            claim[1] = claim[1].strip()
            claims_dic[claim[0]] = claim[1]

    header = sdjwt.Header(settings.alg, settings.typ)
    payload = sdjwt.Payload(12345678, 12345678, settings.sub, settings.aud, claims_dic)

    enc_header = encode64_header(header)
    enc_payload = encode64_payload(payload)
    signature = create_signature(enc_header, enc_payload)
    draft_sdjwt = sdjwt.SD_JWT(enc_header, enc_payload, signature)
    sd_jwt = build_SDJWT(draft_sdjwt)
    return sd_jwt
       

def parse_SDJWT_to_JSON(sd_jwt):
    pass

jwt = parse_data_to_SDJWT("data/text/sample1.txt")
print(jwt)