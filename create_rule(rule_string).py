import ast

def create_rule(rule_string):
    tree = ast.parse(rule_string, mode='eval')  # Parses rule string to AST
    return build_ast(tree.body)  # Build custom AST using helper function

def build_ast(node):
    if isinstance(node, ast.BoolOp):
        return ast('operator', left=build_ast(node.values[0]), right=build_ast(node.values[1]), value=node.op.__class__.__name__)
    elif isinstance(node, ast.Compare):
        left = ast('operand', value=node.left.id)
        right = ast('operand', value=node.comparators[0].n)
        return ast('operator', left=left, right=right, value=node.ops[0].__class__.__name__)
    
