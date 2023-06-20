def find_largest(lst: list):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

def find_smallest(lst: list):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

def is_integer_in_list(x: int, lst: list):
    for num in lst:
        if x == num:
            return True
    