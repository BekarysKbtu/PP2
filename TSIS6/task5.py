def all_elements_true(tup):
    return all(tup)

my_tuple = tuple(map(int, input().split()))
if all_elements_true(my_tuple):
    print("All elements of the tuple are true.")
else:
    print("Not all elements of the tuple are true.")
