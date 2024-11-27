def print_numbers_skip_7(start, end):
    for num in range(start, end + 1):
        if num % 7 != 0:
            print(num, end=" ")
    print()

start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))
print_numbers_skip_7(start, end)

# print("data", sep="" end=" ")
# print(1, 2, sep=" ", end="\n")
# print(3,4)
