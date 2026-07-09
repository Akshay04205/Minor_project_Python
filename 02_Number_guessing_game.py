import random
while True:

    comp = random.randint(1,10)

    print("WELCOME TO THE NUMBER GUESSING GAME")
    #hint 
    if comp <= 5:
        print("HINT: the number is Lower(less than 5)")
    else:
        print("HINT: the number is Higher(greater than 5)")
        
    user = int(input("Guess any number between 1 to 10: "))

    if user >= 11:
        print("Invalid, Guess only in between 1 to 10")
        exit()
    if comp==user:
        print("YAHHHH!, You WON",comp)
    else:
        print("NO, You loss")
        print("The Number is: ",comp)

    retry = input("Retry? (y/n): ")
    if retry.lower() != "y":
        
        print("See you again")
        break