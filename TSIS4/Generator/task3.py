def divisible_by_3_and_4(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

start = int(input("Print start number: "))
end = int(input("Print end number: "))
for num in divisible_by_3_and_4(start, end):
    print(num)
