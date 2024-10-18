class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.node_type == "operator":
            return f"({self.left} {self.value} {self.right})"
        return str(self.value)

def parse_rule(rule_str):
    rule_str = rule_str.replace(" ", "")
    if "AND" in rule_str:
        left_str, right_str = rule_str.split("AND", 1)
        return Node("operator", parse_rule(left_str), parse_rule(right_str), "AND")
    elif "OR" in rule_str:
        left_str, right_str = rule_str.split("OR", 1)
        return Node("operator", parse_rule(left_str), parse_rule(right_str), "OR")
    else:
        return Node("operand", value=rule_str)

def evaluate_condition(condition, user_data):
    if ">" in condition:
        left, right = condition.split(">")
        left = left.strip().strip('()')
        right = int(right)
        return user_data[left] > right
    elif "=" in condition:
        left, right = condition.split("=")
        left = left.strip().strip('()')
        right = right.strip().strip("'")
        return user_data[left] == right
    return False

def evaluate(ast, user_data):
    if ast.node_type == "operator":
        left_result = evaluate(ast.left, user_data)
        right_result = evaluate(ast.right, user_data)
        return left_result and right_result if ast.value == "AND" else left_result or right_result
    else:
        return evaluate_condition(ast.value, user_data)

if __name__ =="__main__":
    while True:
        print("\n1. Create Rule")
        print("2. Combine Rules")
        print("3. Evaluate Rule")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            rule_str = input("Enter rule string: ")
            ast = parse_rule(rule_str)
            print("AST:", repr(ast))
        
        elif choice == '2':
            rules = input("Enter rules separated by commas: ").split(',')
            combined_ast = parse_rule(rules[0].strip())
            for rule in rules[1:]:
                combined_ast = Node("operator", combined_ast, parse_rule(rule.strip()), "OR")
            print("Combined AST:", repr(combined_ast))
        
        elif choice == '3':
            ast_str = input("Enter AST string: ")
            user_data = eval(input("Enter user data (e.g., {'age': 35, 'department': 'Sales'}): "))
            ast = parse_rule(ast_str)
            result = evaluate(ast, user_data)
            print("Evaluation Result:", result)

        elif choice == '4':
            break
        
        else:
            print("Invalid option, please try again.")



