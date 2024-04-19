def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers_list = list(map(int, input().split()))
print(multiply_numbers(numbers_list))
