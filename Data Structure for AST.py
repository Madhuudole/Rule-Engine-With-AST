class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # Can be 'operator' or 'operand'
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value (for 'operand' node)

    def __repr__(self):
        return f"{self.node_type}: {self.value}" if self.node_type == 'operand' else f"({self.left} {self.value} {self.right})"
