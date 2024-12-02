import hashlib

# Helper function to calculate a hash
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to construct a Merkle Tree and return the Merkle Root
def construct_merkle_tree(transactions):
    tree = [[(calculate_hash(tx), i) for i, tx in enumerate(transactions)]]
    
    # Build the tree layer by layer
    while len(tree[-1]) > 1:
        current_layer = tree[-1]
        next_layer = []
        
        for i in range(0, len(current_layer), 2):
            left_node = current_layer[i]
            if i + 1 < len(current_layer):
                right_node = current_layer[i + 1]
            else:
                # Duplicate the last node if there's an odd number of nodes
                right_node = left_node
            
            # Hash the concatenation of left and right child nodes
            combined_hash = calculate_hash(left_node[0] + right_node[0])
            next_layer.append((combined_hash, (left_node[1], right_node[1])))  # Store child positions
            
        tree.append(next_layer)
    
    # The last remaining node is the Merkle Root
    merkle_root = tree[-1][0][0]
    return merkle_root, tree

# Function to validate transactions and identify tampering
def validate_transactions(transactions, merkle_root, tree):
    # Rebuild the Merkle Tree using the current transactions
    rebuilt_merkle_root, _ = construct_merkle_tree(transactions)
    
    # Compare the original and rebuilt Merkle Roots
    if rebuilt_merkle_root != merkle_root:
        print("\n[ALERT] Malicious attempt detected! Transactions have been tampered with.")
        return False
    print("\nAll transactions are valid. No tampering detected.")
    return True

# Example usage
if __name__ == "__main__":
    # Original set of transactions
    transactions = [
        "Product ID:P123:Factory A",
        "Product Name:T-Shirt:Warehouse B",
        "Product Quantity:10:Store C",
        "Product Color:White: Retailer-Mirpur",
        "Product Brand:MENS CLUB:Delivered Customer"
    ]
    
    # Construct the original Merkle Tree and get the Merkle Root
    merkle_root, tree = construct_merkle_tree(transactions)
    
    print("Original Transactions:")
    for tx in transactions:
        print(f"- {tx}")
    
    # Print the original Merkle Root
    print("\nOriginal Merkle Root:", merkle_root)
    
    # Simulate a malicious modification
    tampered_transactions = transactions.copy()
    #tampered_transactions[2] = "Charlie pays Dave 50 BTC"  # Malicious modification
    tampered_transactions[2] = input("Hi-I am - Melicious - would like to Tampered::= ")
    
    print("\nTampered Transactions:")
    for tx in tampered_transactions:
        print(f"- {tx}")
    
    # Validate the tampered transactions against the original Merkle Root
    is_valid = validate_transactions(tampered_transactions, merkle_root, tree)
    
    if not is_valid:
        print("\n[INFO] Block rejected due to tampered transactions.")
    else:
        print("\n[INFO] Block accepted as valid.")
