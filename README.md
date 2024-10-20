# Rule-Engine-With-AST

Developing a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine
user eligibility based on attributes like age, department, income, spend etc.The system can use
Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic
creation,combination, and modification of these rules.
Data Structure:
● Defining a data structure to represent the AST.
● The data structure should allow rule changes
● E,g One data structure could be Node with following fields
○ type: String indicating the node type ("operator" for AND/OR, "operand" for
conditions)
○ left: Reference to another Node (left child)
○ right: Reference to another Node (right child for operators)
○ value: Optional value for operand nodes (e.g., number for comparisons)
Data Storage
● Define the choice of database for storing the above rules and application metadata
● Define the schema with samples.
Sample Rules:
● rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND
department = 'Marketing')) AND (salary > 50000 OR experience >
5)"
● rule2 = "((age > 30 AND department = 'Marketing')) AND (salary >
20000 OR experience > 5)"
API Design:
1. create_rule(rule_string): This function takes a string representing a rule (as
shown in the examples) and returns a Node object representing the corresponding AST.
2. combine_rules(rules): This function takes a list of rule strings and combines them
into a single AST. It should consider efficiency and minimize redundant checks. You can
explore different strategies (e.g., most frequent operator heuristic). The function should
return the root node of the combined AST.
3. evaluate_rule(JSON data): This function takes a JSON representing the combined
rule's AST and a dictionary data containing attributes (e.g., data = {"age": 35,
"department": "Sales", "salary": 60000, "experience": 3}). The
function should evaluate the rule against the provided data and return True if the user is
of that cohort based on the rule, False otherwise.
Test Cases:
1. Create individual rules from the examples using create_rule and verify their AST
representation.
2. Combine the example rules using combine_rules and ensure the resulting AST
reflects the combined logic.
3. Implement sample JSON data and test evaluate_rule for differdifferent scenarios.
4. Explore combining additional rules and test the functionality.      


DOCKER FILE
docker-compose.yml
version: '3'
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data

  backend:
    build: ./backend
    ports:
      - "5000:5000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"

volumes:
  db-data:


Here’s a basic `README.md` template for your project, covering **Prerequisites**, **Setup Instructions**, and other necessary information to help users get started with the rule engine application using AST:

---

# Rule Engine with AST

This project is a simple 3-tier rule engine application that dynamically creates and evaluates rules using an Abstract Syntax Tree (AST). It allows the user to define conditional rules based on attributes like age, department, income, and more, and then evaluate them against provided data.

## Features

- **Rule Creation**: Dynamically create rules from strings and represent them as ASTs.
- **Rule Combination**: Combine multiple rules into a single AST using logical operators like `AND` and `OR`.
- **Rule Evaluation**: Evaluate the combined rules against user data to determine eligibility.
- **Error Handling**: Validates rule syntax and handles invalid input gracefully.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8+**: You can download Python from [python.org](https://www.python.org/downloads/).
- **Virtual Environment (optional)**: It is recommended to set up a virtual environment to manage dependencies.
- **pip**: Python’s package installer. It usually comes with Python installations.
- **VS Code (optional)**: You can use any code editor, but VS Code is recommended for better debugging and code management.


## Overview
This application is a rule engine that determines user eligibility based on attributes such as age, department, salary, and experience. It uses an Abstract Syntax Tree (AST) to represent and manage conditional rules, allowing for dynamic rule creation, combination, and evaluation.

![Screenshot 2024-10-20 155506](https://github.com/user-attachments/assets/0d0f06ce-d7ee-4335-8361-cc208a23be4a)

## Features
Create Rules: Define rules using a string format that gets converted into an AST.
![Screenshot 2024-10-20 155736](https://github.com/user-attachments/assets/ed8f1d98-189c-4f70-9785-dad16e12f99e)
Combine Rules: Combine multiple rules into a single AST for more complex evaluations.
![Screenshot 2024-10-20 155803](https://github.com/user-attachments/assets/c3e1d31c-2d40-4037-a863-ec5d3dcd4ac1)
Evaluate Rules: Check if the given data meets the criteria defined by the AST.
![Screenshot 2024-10-20 155821](https://github.com/user-attachments/assets/33bece5a-1503-4a44-8f11-63ab783bd2e0)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
```

### 2. Set Up Virtual Environment (Optional but Recommended)

To avoid conflicts between dependencies, it's recommended to set up a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
# or
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, add the following dependencies (if needed):

```bash
pip install ast
```

### 4. Running the Application

To run the application and test the rule engine:

```bash
python rule_engine.py
```

Ensure your rules are properly defined, and you can test the functionality with some sample rules as follows:

### Sample Usage

#### Rule Creation

```python
rule_string = "(age > 30 AND department == 'Sales')"
ast_root = create_rule(rule_string)
print(ast_root)  # Outputs the AST representation of the rule
```

#### Rule Combination

```python
rule1 = "(age > 30 AND department == 'Sales')"
rule2 = "(age < 25 AND department == 'Marketing')"
combined_ast = combine_rules([rule1, rule2])
```

#### Rule Evaluation

```python
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(combined_ast, data)
print(result)  # Outputs True or False based on the data
```

## Code Structure

```
├── rule_engine.py         # Main code for the rule engine logic
├── test_cases             # Directory for unit tests
├── requirements.txt       # List of Python dependencies
├── README.md              # This file
```

### Function Overview

- **create_rule(rule_string)**: Converts a string rule into an AST.
- **combine_rules(rules)**: Combines multiple rule ASTs using `OR`.
- **evaluate_rule(ast_node, data)**: Evaluates an AST against input data and returns whether it satisfies the conditions.

## Tests

Run the tests to ensure that the rule engine works as expected:

```bash
python -m unittest discover -s test_cases
```

### Example Test Cases:

1. Test individual rule creation and its AST representation.
2. Test combining multiple rules using the `combine_rules` function.
3. Test evaluating a combined AST against different sets of user data.

## Notes

- Ensure that rules are provided in a valid format for the parser to work.
- This project is a simple demo of rule evaluation logic and can be extended to support more complex operators or custom logic.

## License

This project is licensed under the MIT License.

---

### Additional Suggestions:
- Update the `requirements.txt` if there are specific libraries (like `ast`) needed.
- If you plan to containerize this project (e.g., with Docker), add a section on Docker setup and commands.









