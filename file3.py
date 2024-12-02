import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

transaction = [
    "ProductID:P123:Factory A",
    "ProductName:T-Shirt:Warehouse B",
    "ProductColor:White:Store C",
    "ProductBrand:MENZCLUB"
             ]

tree = [[(calculate_hash(transaction),i) for i, transaction in enumerate(transaction)]]
for leaf in tree[0]:
    print(leaf)

