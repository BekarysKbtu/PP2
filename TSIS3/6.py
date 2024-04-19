nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_nums = filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, nums)

print("Prime numbers:", list(prime_nums))
