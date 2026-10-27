valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("One More!")
            n = int(input("Enter a number: "))
        valid = True
        print("BYE")
    except ValueError:
        print("Invalid")
        