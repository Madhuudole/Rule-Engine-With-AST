def evaluate_rule(ast_node, data):
    if ast_node.node_type == 'operand':
        return data[ast_node.value]  # Return the value from data

    elif ast_node.node_type == 'operator':
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)

        if ast_node.value == 'And':
            return left_result and right_result
        elif ast_node.value == 'Or':
            return left_result or right_result
        elif ast_node.value == 'Gt':  # Greater than
            return left_result > right_result
        elif ast_node.value == 'Lt':  # Less than
            return left_result < right_result
        
