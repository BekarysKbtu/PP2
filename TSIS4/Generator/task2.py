def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input())

# Print even numbers separated by commas
even_numbers = (str(num) for num in even_numbers_generator(n))
print(" ".join(even_numbers))
