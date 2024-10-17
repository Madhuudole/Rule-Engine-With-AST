# Function to combine multiple rules into a single AST using OR
import ast
def combine_rules(rules):
    if not rules:
        raise ValueError("No rules provided for combination.")
    
    # Start with the AST of the first rule
    combined_ast = create_rule(rules[0])

    # For each additional rule, combine using the OR operator
    for rule in rules[1:]:
        rule_ast = create_rule(rule)
        # Combine the current combined_ast with the new rule_ast using OR
        combined_ast = ast('operator', left=combined_ast, right=rule_ast, value='OR')

    return combined_ast
