import hashlib
data = "Blockchain Technology"
hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()
print("Blockchain Technology Hash Formate ..",hash_hex)