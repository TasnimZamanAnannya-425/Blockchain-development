import hashlib
data = "ProductID:P123:Factory A"
hash_object = hashlib.sha256(data.encode())
print("encode =",hash_object())
hash_hex = hash_object.hashdigest()
print("Hashing of the BlockData =",hash_hex)