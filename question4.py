def find_maximum():
    numbers = [] # mwangi - we initiate an empty array that will hold the user's input values.

    for i in range(1, 6): # range () method loops over numbers inclusive of 1 but exclusive of 6. 
        # while loop helps us loop indefinately untill we have the numbers required after which e brea the loop using a break statement.
        while True: 
            #try-except block to help manage errors.
            try:
                # mwangi- Check if the input is a number and within the range of 1 to 100
                num = float(input(f"Enter number {i}: "))
                numbers.append(num) # we add the user's inputs into the numbers array after which we find the maximum number.
               #break statement for closing or terminating the while loop.
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    print(f"The maximum value is: {max(numbers)}")

find_maximum()
