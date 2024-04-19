def squares_generator(n):
    for i in range(n):
        yield i**2

n = int(input())
for square in squares_generator(n):
    print(square)
