def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

# Test the generator with a for loop
n = int(input())
for num in numbers_down_to_zero(n):
    print(num)
