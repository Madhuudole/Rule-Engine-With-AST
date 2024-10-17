import ast

# Define the ASTNode class
class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # Can be 'operator' or 'operand'
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value (for 'operand' node) or operator type

    def __repr__(self):
        return f"{self.node_type}: {self.value}" if self.node_type == 'operand' else f"({self.left} {self.value} {self.right})"

# Function to create the AST from rule string
def create_rule(rule_string):
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

# Combine multiple rules into a single AST by connecting them with the OR operator
def combine_rules(rules):
    combined_node = None
    for rule in rules:
        ast_node = create_rule(rule)
        if combined_node is None:
            combined_node = ast_node
        else:
            combined_node = ASTNode('operator', left=combined_node, right=ast_node, value='OR')
    return combined_node

# Evaluate the AST against provided data
def evaluate_rule(ast_node, data):
    if ast_node.node_type == 'operand':
        # For operands, retrieve the value from the data dictionary
        return data.get(ast_node.value, None)
    
    if ast_node.value == 'AND':
        # Evaluate left and right children for AND operation
        return evaluate_rule(ast_node.left, data) and evaluate_rule(ast_node.right, data)
    
    if ast_node.value == 'OR':
        # Evaluate left and right children for OR operation
        return evaluate_rule(ast_node.left, data) or evaluate_rule(ast_node.right, data)
    
    # Evaluate comparisons
    if ast_node.value in ('>', '<', '=='):
        left_value = data.get(ast_node.left.value)
        right_value = ast_node.right.value if isinstance(ast_node.right.value, (int, str)) else data.get(ast_node.right.value)
        if ast_node.value == '>':
            return left_value > right_value
        elif ast_node.value == '<':
            return left_value < right_value
        elif ast_node.value == '==':
            return left_value == right_value

    return False  # Default return value for unmatched cases

# Example rules
rules = [
    "(age > 30 and department == 'Sales')",
    "(age < 25 and department == 'Marketing')",
    "(salary > 50000 or experience > 5)"
]

# Combine rules into a single AST
combined_ast = combine_rules(rules)

# Print the combined AST representation
print("Combined AST:")
print(combined_ast)

# Example data to evaluate against
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Evaluate the combined AST against the data
result = evaluate_rule(combined_ast, data)

# Print the evaluation result
print("Evaluation result:", result)
