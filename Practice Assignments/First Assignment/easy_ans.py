## Name: <Name of the student>

# NOTE: Write your Algorithm as comments inside the function.


# Question 1:
def find_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Question 2:
def withdrawal(amount):
    notes = [2000, 500, 100]
    if amount % 100 != 0:
        return {}
    resp = {"2000": 0, "500": 0, "100": 0}
    for note in notes:
        resp[str(note)] = amount // note
        amount = amount % note
    return resp


## 📌📌 NOTE: Please donot change the code below.
## This code is used to test your functions.
if __name__ == "__main__":

    def test(cases, func):
        for n, expected in cases:
            recieved = func(n)
            if type(recieved) != type(expected):
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
            elif recieved != expected:
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
        print(f"✅ All Test passed for {func.__name__}")
        return True

    factorial_test_cases = [(5, 120), (3, 6), (0, 1)]

    withdrawal_test_cases = [
        (1000, {"2000": 0, "500": 2, "100": 0}),
        (2800, {"2000": 1, "500": 1, "100": 3}),
        (0, {"2000": 0, "500": 0, "100": 0}),
        (250, {}),
    ]

    test(factorial_test_cases, find_factorial)
    test(withdrawal_test_cases, withdrawal)
