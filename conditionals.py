name = input("Hi, what is your name? ")
userNumber = int(input(f"{name}, enter an integer between 1 and 100: "))

if userNumber % 2 == 0:
    if 2 <= userNumber <= 24:
        print(f"{userNumber} is even and less than 25")
    elif 26 <= userNumber <= 60:
        print(f"{userNumber} is even and between 26 and 60 inclusive")
    elif userNumber > 60:
        print(f"{userNumber} is even and greater than 60")
elif userNumber % 2 == 1:
    if userNumber < 60:
        print(f"{userNumber} is odd and less than 60")
    elif userNumber > 60:
        print(f"{userNumber} is odd and greater than 60")
