import random
from time import sleep

isRaining = input("Is raining? Yes or No: ").lower()

if(isRaining == "yes"):
    haveUmbrella = input("Have umbrella? Yes or No: ").lower()
    if(haveUmbrella == "no"):
        print("Wait a while ...")
        while isRaining == "yes":
            # ta linijka poniżej ...
            #isRaining = input("Is raining? Yes or No: ").lower()

            # ... albo te dwie poniżej :)
            isRaining = random.choice(["yes", "no"]) # importowanie random potrzebne tylko do tej linii
            sleep(0.5) # importowanie sleep potrzebne tylko do tej linii

print("Go outside.")
