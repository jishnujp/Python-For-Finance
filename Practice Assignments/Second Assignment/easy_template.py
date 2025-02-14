## Name: <Name of the student>

# NOTE: Write your Algorithm as comments inside the function.


# Question 1:
def replace_vowels(s):
    pass


# Question 2:
def biggest_candle(ohlc_data):
    pass


# Question 3
def number_guessing_game():
    pass


## 📌📌 NOTE: Please donot change the code below.
## This code is used to test your functions.
if __name__ == "__main__":
    # Test cases for replace_vowels
    if replace_vowels("apple") != "*ppl*":
        print("❌ Test 1 failed for replace_vowels")
    else:
        print("✅ Test 1 passed for replace_vowels")

    if replace_vowels("banana") != "b*n*n*":
        print("❌ Test 2 failed for replace_vowels")
    else:
        print("✅ Test 2 passed for replace_vowels")

    if replace_vowels("mango") != "m*ng*":
        print("❌ Test 3 failed for replace_vowels")
    else:
        print("✅ Test 3 passed for replace_vowels")

    print("*" * 30)

    # Test cases for biggest_candle

    if biggest_candle(
        [
            [200, 220, 210, 215],
            [205, 240, 200, 230],
            [210, 250, 195, 245],
            [215, 235, 220, 225],
        ]
    ) != [210, 250, 195, 245]:
        print("❌ Test 1 failed for biggest_candle")
    else:
        print("✅ Test 1 passed for biggest_candle")

    if biggest_candle(
        [
            [100, 110, 95, 105],
            [102, 115, 98, 110],
            [103, 120, 100, 115],
            [101, 108, 99, 107][105, 110, 100, 105],
        ]
    ) != [103, 120, 100, 115]:
        print("❌ Test 2 failed for biggest_candle")
    else:
        print("✅ Test 2 passed for biggest_candle")
