import ast

# Define the ASTNode class
class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # Can be 'operator' or 'operand'
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value (for 'operand' node) or operator type

    def __repr__(self):
        if self.node_type == 'operand':
            return f"Operand({self.value})"
        else:
            return f"({self.left} {self.value} {self.right})"

# Function to create the AST from rule string
def create_rule(rule_string):
    # Replace logical operators with Python equivalents
    rule_string = rule_string.replace("AND", "and").replace("OR", "or")
    
    tree = ast.parse(rule_string, mode='eval')  # Parse the rule string to AST
    return build_ast(tree.body)  # Build custom AST using helper function

# Helper function to build the AST from Python's AST
def build_ast(node):
    if isinstance(node, ast.BoolOp):
        left_node = build_ast(node.values[0])
        right_node = build_ast(node.values[1])
        op_type = 'AND' if isinstance(node.op, ast.And) else 'OR'
        return ASTNode('operator', left=left_node, right=right_node, value=op_type)
    elif isinstance(node, ast.Compare):
        left_operand = node.left.id  # Assuming it's a variable like 'age'
        right_operand = node.comparators[0].n if isinstance(node.comparators[0], ast.Num) else node.comparators[0].s
        op_type = '>' if isinstance(node.ops[0], ast.Gt) else '<' if isinstance(node.ops[0], ast.Lt) else '=='
        return ASTNode('operator', left=ASTNode('operand', value=left_operand), right=ASTNode('operand', value=right_operand), value=op_type)
    else:
        raise ValueError("Unsupported operation in rule")

# Example rule string
rule_string = "(age > 30 AND department == 'Sales')"

# Create AST from rule string
ast_root = create_rule(rule_string)

# Print the AST representation
print("AST Representation:")
print(ast_root)
