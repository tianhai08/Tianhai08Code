
def fun_sum_digits(number):
    return sum(int(digit) for digit in str(number))

print(fun_sum_digits(12345))
