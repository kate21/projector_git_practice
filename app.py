#Input - numbers and operation - sum, substraction, division

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
elif '/' in input_data:
    numbers = input_data.split("/")
    numbers = [int(num) for num in numbers]
    res = numbers[0]
    for num in numbers[1:]:
        res /= num
    print(f'Result: {res}')
else:
    print("Operation not supportable")