import base58

# Input your mnemonic key from phantom
byte_array = base58.b58decode('YOUR_SECRET_KEY')

json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
print(json_string)
