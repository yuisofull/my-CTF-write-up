import random
# def generate_random_number():#3x1, 4x2 ...9x7
#     while True:
#         num = random.randint(100, 999)
#         first_digit = num // 100
#         last_digit = num % 10
#         if abs(first_digit - last_digit) > 1:
#             return num

# number = generate_random_number()
# num1 = int(''.join(sorted(str(number), reverse=True)))
# num2 = int(''.join(sorted(str(number))))
# diff = abs(num1 - num2)
# rev_diff = int(str(diff)[::-1])
# number = diff + rev_diff

# print(number)



def generate_random_number_again():
    while True:
        num = random.randint(1000, 9999)
        if num % 1111 != 0:
            return num
number = generate_random_number_again()
i = 0
while number != 6174:
    digits = [int(d) for d in str(number)]
    digits.sort()
    smallest = int(''.join(map(str, digits)))
    digits.reverse()
    largest = int(''.join(map(str, digits)))
    number = largest - smallest
    i += 1
print(i)