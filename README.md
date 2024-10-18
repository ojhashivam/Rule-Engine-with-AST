# Rule Engine Application
The Rule Engine Application is a Python-based tool that allows users to create, combine, and evaluate logical rules using an Abstract Syntax Tree (AST). It supports basic logical operations such as AND and OR, and allows for the evaluation of conditions against user-provided data.

# Features
  Create individual rules using conditions.
  Combine multiple rules using logical operators (AND, OR).
  Evaluate rules against user data.
  Display the Abstract Syntax Tree (AST) representation of rules.

# Requirements
  Python 3.7+

# Installation
  Clone this repository or download the code files.
  Ensure you have Python installed on your system.
  Navigate to the directory containing the script.

# Usage
Run the application:
   ```bash
   python main.py


# You will be presented with a menu with the following options:

1: Create a new rule
2: Combine multiple rules
3: Evaluate a rule against data
4: Exit the application
Follow the prompts to create or evaluate rules.

Rule Format
  A rule can be expressed in the following format:
  Conditions can be combined using AND or OR.

  Example conditions:
  age > 30
  department = 'Sales'

  Example rule: (age > 30 AND department = 'Sales')

  User Data Format
  When prompted for user data, enter a dictionary format, e.g.:
  python
  Copy code

  {'age': 35, 'department': 'Sales'}
  Example
  Here is an example of how to create and evaluate a rule:
  
  Select option 1 to create a new rule.
  Enter a rule string, e.g., (age > 30 AND department = 'Sales').
  Select option 3 to evaluate the rule.
  Enter the user data, e.g., {'age': 35, 'department': 'Sales'}.
  The application will evaluate the rule against the user data and display the result.
