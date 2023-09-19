def multiplication(a, b1):
    b1.reverse()
    b2 = [(0) for i in range(len(b1)+1)]
    for i in range(len(b1)):
        c = a * b1[i] + b2[i]
        b2[i] = 0
        if c > 9:
            c_tens = c // 10
            c_ones = c - 10 * ( c // 10 )
            b2[i+1] += c_tens
            c = c_ones
        b1[i] = c
    b1.reverse()
    return b1

def list_from_number(x):
    list1 = [int(i) for i in str(x)]
    list1 = [0, 0, 0] + list1
    return list1

def number_from_list(x):
    result = 0
    for i in range(len(x)):
        result += (x[i] * 10 ** (len(x) - i - 1))
    return int(result)

# test1 = 10
# test1_list = list_from_number(test1)
# test1_square_list = multiplication(test1, test1_list)
# test1_square = number_from_list(test1_square_list)
# print(test1_square)

def factorial1(n):
    number1 = 1
    for i in range(n):
        number1 = list_from_number(number1)
        factorial_list = multiplication(i + 1, number1)
        number1 = number_from_list(factorial_list)
    return number1

f = int(input("Enter a number: "))
fact = 1
for i in range(1, f + 1):
    fact = fact * i
print(f"The factorial of {f} (fast method) is: ", end = "")
print(fact)

print(f"The factorial of {f} (slow method) is: ", end = "")
print(factorial1(f))