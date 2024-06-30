# calculate_factorial.py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
