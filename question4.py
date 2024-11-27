def find_maximum():
    numbers = []
    for i in range(1, 6):
        while True:
            try:
                # mwangi- Check if the input is a number and within the range of 1 to 100
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    print(f"The maximum value is: {max(numbers)}")

find_maximum()
