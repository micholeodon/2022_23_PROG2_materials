nieMoge = True
nieChce = True

if nieMoge and nieChce:
    print("Nie moge i nie chce!")
elif nieMoge and not nieChce:
    print("Nie moge ale chce!")
elif not nieMoge and nieChce:
    print("Nie chce choc moge!") 
elif not nieMoge and not nieChce:
    print("Moge i chce!")
else:
    print("?????") # nigdy tu nie wejdziemy

print("Koniec.")

