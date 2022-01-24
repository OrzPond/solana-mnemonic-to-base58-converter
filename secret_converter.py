import base58

# Input your mnemonic key from phantom
key = base58.b58decode('YOUR_SECRET_KEY')

key_in_base58 = "[" + ",".join(map(lambda b: str(b), key)) + "]"

print(key_in_base58)
