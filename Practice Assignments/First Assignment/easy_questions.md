## Easy Assignment Questions
Instructions:

1. Use the template file provided to write your code.
2. Do not modify any function signature.
3. Write your logic inside the function as comments.


## Question 1: Find Factorial
Write a function `find_factorial` that takes an integer as input and returns its factorial.

Example:
- `find_factorial(5)`  # Returns 120
- `find_factorial(3)`  # Returns 6

**Function Signature:** `def find_factorial(n: int) -> int:`

## Question 2: ATM Withdrawal 
Write a function `withdrawal` that takes an integer as input and returns the denominations of notes to be dispensed. The function should return the minimum number of notes. The available denominations are ₹2000, ₹500, and ₹100.
If the amount cannot be withdrawn using the available denominations, return an empty dictionary.

Example:
- `withdrawal(2800)`  # Returns {'2000': 1, '500': 1, '100': 3}
- `withdrawal(1500)`  # Returns {'2000': 0, '500': 3, '100': 0}

**Function Signature:** `def withdrawal(amount: int) -> Dict[str, int]:`

