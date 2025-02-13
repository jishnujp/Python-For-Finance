## Name: <Name of the student>

# NOTE: Write your Algorithm as comments inside the function.


# Question 1:
def add_numbers(a, b):
    pass


# Question 2:
def calculate_simple_interest(P, R, T):
    pass


def check_number(n):
    pass


## 📌📌 NOTE: Please donot change the code below.
## This code is used to test your functions.
if __name__ == "__main__":

    def test(cases, func):
        for n, expected in cases:
            recieved = func(*n)
            if type(recieved) != type(expected):
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
            elif recieved != expected:
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
        print(f"✅ All Test passed for {func.__name__}")
        return True

    add_numbers_test_cases = [((2, 3), 5), ((3, 4), 7), ((0, 0), 0)]
    simple_interest_test_cases = [
        ((1000, 5, 2), 100),
        ((2000, 10, 3), 600),
        ((0, 0, 0), 0),
    ]
    check_number_test_cases = [((2,), "Positive"), ((-3,), "Negative"), ((0,), "Zero")]

    test(add_numbers_test_cases, add_numbers)
    test(simple_interest_test_cases, calculate_simple_interest)
    test(check_number_test_cases, check_number)
