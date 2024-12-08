<<<<<<< HEAD
#Input - numbers and operation - sum, substraction, multyplication
=======
#Input - numbers and operation - sum, substraction, division
>>>>>>> feat-div

input_data = input("Enter your operation:")

if '+' in input_data:
    numbers = input_data.split("+")
    numbers = [int(num) for num in numbers]
    res = sum(numbers)
    print(f'Result: {res}')
elif '-' in input_data:
    numbers = input_data.split("-")
    numbers = [int(num) for num in numbers]
    res = numbers[0] - sum(numbers[1:])
    print(f'Result: {res}')
<<<<<<< HEAD
elif '*' in input_data:
    numbers = input_data.split("*")
    res = 1
    for num in numbers:
        res *= int(num)
=======
elif '/' in input_data:
    numbers = input_data.split("/")
    numbers = [int(num) for num in numbers]
    res = numbers[0]
    for num in numbers[1:]:
        res /= num
>>>>>>> feat-div
    print(f'Result: {res}')
else:
    print("Operation not supportable")