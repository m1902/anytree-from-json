from anytree import Node, RenderTree
import json

# Recursive function to convert JSON structure into Anytree nodes
def json_to_anytree(node_data, parent=None):
    # Create the current node with its type and label
    node = Node(f"{node_data['type']} ({node_data['label']})", parent=parent)

    # Recursively create child nodes
    for child in node_data.get('children', []):
        json_to_anytree(child, node)

    return node  # Return the root node of the tree (or subtree)


# Load the tree from the JSON file
with open('tree_output.json', 'r') as f:
    tree_data = json.load(f)

# Convert the JSON data to anytree format
root = json_to_anytree(tree_data)

# Print the root name
print(f"Root name: {root.name}")

print("Full tree:")
# Print the tree structure
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")
