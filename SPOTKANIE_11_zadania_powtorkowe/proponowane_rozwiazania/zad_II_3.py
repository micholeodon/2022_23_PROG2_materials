
print("You see a guy. ", end = '')


while True:
    ans1 = input("Is he looking at you? ")
    ans2 = input("Is he cute? ")

    if ans1.lower() == "yes":
        lookingOrNot = "looking"
    elif ans1.lower() == "no":
        lookingOrNot = "not looking"
    else:
        print("I don't understand. ")

    if ans2.lower() == "yes":
        cuteOrNot = "cute"
        break
    elif ans1.lower() == "no":
        cuteOrNot = "not cute"
        break
    else:
        print("I don't understand. ")


print(f"Ok ... So you see a guy, he is {lookingOrNot} at you, and he is {cuteOrNot}.")
print("Avoid eye contact!")