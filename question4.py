def find_maximum():
    """Prompt the user to enter 5 numbers and find the maximum value."""
    numbers = []
    for i in range(1, 6):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    print(f"The maximum value is: {max(numbers)}")

# Example usage
find_maximum()
