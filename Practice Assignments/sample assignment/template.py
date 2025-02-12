## Name: <Name of the student>

# NOTE: Write your Algorithm as comments inside the function.


# Question 1:
def is_even(n):
    pass


# Question 2:
def is_prime(n):
    pass


## 📌📌 NOTE: Please donot change the code below.
## This code is used to test your functions.
if __name__ == "__main__":

    def test(cases, func):
        for n, expected in cases:
            recieved = func(n)
            if type(recieved) != type(expected):
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
            elif func(n) != expected:
                print(f"❌ Test failed for {func.__name__} with input {n}")
                return False
        print(f"✅ All Test passed for {func.__name__}")
        return True

    even_test_cases = [(2, True), (3, False), (0, True)]
    prime_test_cases = [(2, True), (3, True), (4, False)]

    test(even_test_cases, is_even)
    test(prime_test_cases, is_prime)
