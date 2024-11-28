# max()
#input()
#int()
#range()

def max_number():              #try-except block
    number=[]
    for i in range(1, 6):
        while True:
            try:
                num = float((input(f"Enter a number {i}: ")))
                number.append(num)
                break
            except ValueError:
                print("Invalid number")
    print(f"maximun number is : {max(number)}")   #max()
max_number()