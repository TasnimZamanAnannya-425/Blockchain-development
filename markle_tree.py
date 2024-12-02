import hashlib
#from math import ceil

# Helper function to calculate a hash
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to construct a Merkle Tree and return the Merkle Root
def construct_merkle_tree(transactions):
    # Track each transaction's position
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

# Function to trace the position of a specific transaction
def find_transaction_path(tree, transaction_index):
    path = []
    for layer in tree[:-1]:  # Exclude the root layer
        for i, (node, position) in enumerate(layer):
            if transaction_index in (position if isinstance(position, tuple) else [position]):
                sibling_index = i + 1 if i % 2 == 0 else i - 1  # Get sibling
                if sibling_index < len(layer):
                    sibling_hash = layer[sibling_index][0]
                else:
                    sibling_hash = node  # If odd node, sibling is itself
                path.append(sibling_hash)
                transaction_index = position if isinstance(position, tuple) else position
                break
    return path

# Example usage
if __name__ == "__main__":
    transactions = [
        "Product ID:P123:Factory A",
        "Product Name:T-Shirt:Warehouse B",
        "Product Quantity:10:Store C",
        "Product Color:White: Retailer-Mirpur",
        "Product Brand:MENS CLUB:Delivered Customer"
    ]
    
    # Construct the Merkle Tree and get the Merkle Root
    merkle_root, tree = construct_merkle_tree(transactions)
    
    # Print the tree layers
    print("Merkle Tree Layers:")
    for i, layer in enumerate(tree):
        print(f"Layer {i}: {[(node, pos) for node, pos in layer]}")
    
    # Print the Merkle Root
    print("\nMerkle Root:", merkle_root)
    
    # Find the position of a specific transaction and its path
    #transaction_index = 1  # Example: "Bob pays Charlie 5 BTC"
    transaction_index = int(input("Please Track Your Transaction = "))
    path = find_transaction_path(tree, transaction_index)
    
    print(f"\nPath for transaction '{transactions[transaction_index]}':")
    print(path)

