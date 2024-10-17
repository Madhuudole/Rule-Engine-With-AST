from rule_engine import create_rule
import ast
def evaluate_rule(ast_node, data):
    if ast_node.node_type == 'operand':
        # If the value is a string (like 'age'), we retrieve it from the data
        if isinstance(ast_node.value, str):
            return data[ast_node.value]
        # Otherwise, it's a literal (like 30), so we return it directly
        return ast_node.value
    
    # If it's an operator, recursively evaluate the left and right nodes
    left_value = evaluate_rule(ast_node.left, data)
    right_value = evaluate_rule(ast_node.right, data)

    # Perform the operation based on the operator type
    if ast_node.value == 'AND':
        return left_value and right_value
    elif ast_node.value == 'OR':
        return left_value or right_value
    elif ast_node.value == '>':
        return left_value > right_value
    elif ast_node.value == '<':
        return left_value < right_value
    elif ast_node.value == '==':
        return left_value == right_value
    else:
        raise ValueError(f"Unsupported operator: {ast_node.value}")
    
# Function to combine multiple rules into a single AST using OR
def create_rule(rule_string):
    tree = ast.parse(rule_string, mode='eval')  # Parse the rule string to AST
def combine_rules(rules):
    if not rules:
        raise ValueError("No rules provided for combination.")
    
    # Start with the AST of the first rule
    combined_ast = create_rule(rules[0])

    # For each additional rule, combine using the OR operator
    for rule in rules[1:]:
        rule_ast = create_rule(rule)
       
# Example rules
rule1 = "(age > 30 AND department == 'Sales')"
rule2 = "(age < 25 AND department == 'Marketing')"

# Test data to evaluate against
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

