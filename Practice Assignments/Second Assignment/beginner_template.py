## Name: <Name of the student>

# NOTE: Write your Algorithm as comments inside the function.


# Question 1:
def largest(a, b, c):
    pass


# Question 2:
def get_grades(marks):
    pass


# Question 3
def fizz_buzz(n):
    pass


## 📌📌 NOTE: Please donot change the code below.
## This code is used to test your functions.
if __name__ == "__main__":
    # Test cases for largest
    # 1
    if largest(1, 2, 3) != 3:
        print("❌ Test 1 failed for largest")
    else:
        print("✅ Test 1 passed for largest")
    # 2
    if largest(3, 2, 1) != 3:
        print("❌ Test 2 failed for largest")
    else:
        print("✅ Test 2 passed for largest")
    # 3
    if largest(-2.2, 3, 1) != 3:
        print("❌ Test 3 failed for largest")
    else:
        print("✅ Test 3 passed for largest")

    print("*" * 30)

    # Test cases for get_grades
    # 1
    if get_grades(92) != "A":
        print("❌ Test 1 failed for get_grades")
    else:
        print("✅ Test 1 passed for get_grades")
    # 2
    if get_grades(81) != "B":
        print("❌ Test 2 failed for get_grades")
    else:
        print("✅ Test 2 passed for get_grades")
    # 3
    if get_grades(77) != "C":
        print("❌ Test 3 failed for get_grades")
    else:
        print("✅ Test 3 passed for get_grades")
    # 4
    if get_grades(68) != "D":
        print("❌ Test 4 failed for get_grades")
    else:
        print("✅ Test 4 passed for get_grades")
    # 5
    if get_grades(33) != "F":
        print("❌ Test 5 failed for get_grades")
    else:
        print("✅ Test 5 passed for get_grades")

    print("*" * 30)

    # Test cases for fizz_buzz
    # 1
    if fizz_buzz(5) != [1, 2, "Fizz", 4, "Buzz"]:
        print("❌ Test 1 failed for fizz_buzz")
    else:
        print("✅ Test 1 passed for fizz_buzz")

    # 2
    if fizz_buzz(15) != [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
    ]:
        print("❌ Test 2 failed for fizz_buzz")
    else:
        print("✅ Test 2 passed for fizz_buzz")
