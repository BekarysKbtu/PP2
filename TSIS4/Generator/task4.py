def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for square in squares_generator(a, b):
    print(square)
