## Beginner Assignment Questions
Instructions:

1. Use the template file provided to write your code.
2. Do not modify any function signature.
3. Write your logic inside the function as comments.


## Question 1: Largest among three
Write a function `largest` that takes three integers as input and returns the largest number among them.

Example:
- `largest(3, 5, 11)`  # Returns 11
- `largest(10, -2, 0)` # Returns 10

**Function Signature:** `def largest(a, b, c):`


## Question 2: Grade Calculator
Write a function `get_grades` that calculates grades for a subject from the given marks out of 500. The function should return a string indicating the grade based on the following criteria:

- 90% or above: "A"
- 80% - 89%: "B"
- 70% - 79%: "C"
- 60% - 69%: "D"
- Below 60%: "F"

The function should take one input parameter `marks` and return the grade as a string.

Example:
- `get_grades(469)`  # Returns A
- `get_grades(150)` # Returns F

**Function Signature:** `def get_grades(marks) -> string:`


## Question 3: Fizz Buzz
Write a function `fizz_buzz` that takes an integer `n` as input and returns a list of numbers from 1 to `n`. For multiples of 3, the list should have "Fizz" instead of the number. For multiples of 5, the list should have "Buzz". For numbers which are multiples of both 3 and 5, the list should have "FizzBuzz".

Example:
- `fizz_buzz(5)`  # Returns [1, 2, "Fizz", 4, "Buzz"]
- `fizz_buzz(15)` # Returns [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

**Function Signature:** `def fizz_buzz(n):`
