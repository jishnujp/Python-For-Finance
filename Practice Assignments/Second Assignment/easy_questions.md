## Beginner Assignment Questions
Instructions:

1. Use the template file provided to write your code.
2. Do not modify any function signature.
3. Write your logic inside the function as comments.


## Question 1: Replace Vowels
Write a function `replace_vowels` that takes a string as input and replaces every vowel with `*`. The function should return the modified string.

Example:
- `replace_vowels("hello world")`  # Returns "h*ll* w*rld"
- `replace_vowels("apple")` # Returns "*ppl*"

**Function Signature:** `def replace_vowels(s):`



## Question 2: Biggest Candle body
Write a function `volatile_candle` that takes a list of lists(list of  OHLC values) as input and returns the first candle with the biggest volatility. The candle with the biggest volatility is the one with the biggest difference between the High and Low values. The input list will have the following format:
[Open, High, Low, Close]

Example:
- ```python
    volatile_candle([
    [200, 220, 210, 215],
    [205, 240, 200, 230],
    [210, 250, 195, 245],
    [215, 235, 220, 225]
])``` # returns [210, 250, 195, 245]
- ```python
    volatile_candle([
    [100, 110, 95, 105],
    [102, 115, 98, 110],
    [103, 120, 100, 115],
    [101, 108, 99, 107],
    [105, 110, 100, 105]
])``` # returns [103, 120, 100, 115]

**Function Signature:** `def volatile_candle(ohlc_data):`


## Question 3: Number Guessing Game
**NOTE :** There is no test cases for those questions. You can test them by running the function in the terminal.
Write a function `number_guessing_game` that generates a random number between 1 and 100. The function should then let the user guess the number and give hints (higher/lower). The user wins if they guess the number correctly within 10 attempts (returns True); otherwise, they lose (returns False).

Example:
- `number_guessing_game()` # returns True or False based on the user's guesses

**Function Signature:** `def number_guessing_game():`
