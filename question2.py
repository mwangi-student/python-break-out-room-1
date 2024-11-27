def is_sorted(numbers):
    """Check if a list is sorted in ascending order."""
    return numbers == sorted(numbers)

print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False

# my_number=[1,4,6,3,8,9]
# new_number = my_number.sort()