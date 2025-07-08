import secrets
#respon for generating a secret key
key = secrets.token_hex(32)
print(key)
