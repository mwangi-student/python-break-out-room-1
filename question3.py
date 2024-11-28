def print_numbers (start, end): # mwangi -  the start and end here are arguments to the function print_numbers(). Someone else might say they are place holders for the original or actual values from the user.
    for number in range(start, end + 1):
        # mwangi - the if statement checks whether the number provided by the user is divisible by 7. The != operator allows us to print only the numbers not divisible by 7
        # because any number divisible by 7 can retun a " 0 ".
        if number % 7 != 0 :  
            print(number, end=" ") # mwangi - the end=" " methos is a print parameter theat allows us to dictate whether the pring functions creates a new line upon completion or to just create a space after execution.
    print()
# mwangi - by default the input() method recieves the user's input inform of a string. Therefore we need to convert the inputs from strings to integers for the range() method to be executed.
#  To do so, we need the int() method to help us convert the user's input from string to integer.
start = int(input("What is your start Value? ")) 
end = int(input("What is your end Value? "))
print_numbers(start, end)