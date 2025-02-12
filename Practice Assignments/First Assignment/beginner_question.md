## Sample Assignment Questions
Instructions:

1. Use the template file provided to write your code.
2. Do not modify any function definition.
3. Write your logic inside the function as comments.


## Question 1: Add Two Numbers
Write a function `add_numbers` that takes two integers as input and returns their sum.

Example:
- `add_numbers(3, 5)`  # Returns 8
- `add_numbers(10, -2)` # Returns 8

**Function Signature:** `def add_numbers(a: int, b: int) -> int:`


## Question 2: Simple Interest Calculation
Write a function `calculate_simple_interest` that calculates simple interest using the formula:

\[ SI = (P \times R \times T) / 100 \]

Where:
- `P` is the principal amount (int)
- `R` is the rate of interest per year (float)
- `T` is the time in years (int)

The function should take three arguments and return the calculated simple interest as a float.

Example:
- `calculate_simple_interest(1000, 5, 2)`  # Returns 100.0
- `calculate_simple_interest(1500, 4.5, 3)` # Returns 202.5

**Function Signature:** `def calculate_simple_interest(P: int, R: float, T: int) -> float:`


## Question 3: Check if a Number is Positive, Negative, or Zero
Write a function `check_number` that takes an integer as input and returns a string indicating whether the number is "Positive", "Negative", or "Zero".

Example:
- `check_number(5)`  # Returns "Positive"
- `check_number(-3)` # Returns "Negative"
- `check_number(0)`  # Returns "Zero"

**Function Signature:** `def check_number(n: int) -> str:`

