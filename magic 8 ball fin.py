response = ["yes", "no", "most likely", "ask again later", "cannot predict now", "don't count on it", "my sources say no", "very doubtful"]
print("What will you do?\n	1: print all the fortunes\n	2: print a specific fortune\n	3: get a random fortune ")
choice = input("Please choose 1, 2, or 3: ")
if choice == "1":
    print("YOUR FORTUNES")
    for (id, response) in enumerate(response):
        print(f"{id}: {response}")
elif choice == "2":
    chosenResponse = input("Which answer would you like to print?\n	Please choose a number 0 through 7. ")
    if chosenResponse == "0":
        print(response[0])
    elif chosenResponse == "1":
        print(response[1])
    elif chosenResponse == "2":
        print(response[2])
    elif chosenResponse == "3":
        print(response[3])
    elif chosenResponse == "4":
        print(response[4])
    elif chosenResponse == "5":
        print(response[5])
    elif chosenResponse == "6":
        print(response[6])
    elif chosenResponse == "7":
        print(response[7])
    else:
        print("I'm not familiar with that response...")
elif choice == "3":
    import random
    eightBallAnswer = input("What would you like to ask the Magic 8 Ball? ")
    numResponse = len(response)
    responseNum = random.randrange(numResponse)
    print(f"{response[responseNum]}")
else:
    print("I'm not sure what you want me to do...")
    quit()
    


        

