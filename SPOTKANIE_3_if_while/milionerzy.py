pytanie = "Co może zrobić programista?"
odpA = "A. programować"
odpB = "B. dobrze sie bawic"
odpC = "C. jesc"
odpD = "D. zalogowac i spać"

print(pytanie)
print(odpA)
print(odpB)
print(odpC)
print(odpD)
mojaOdp = input("Wybierz odpowiedź: ")
print("Wybrałeś odpowiedź: " + mojaOdp)

if mojaOdp == "A":
    print("Przykro mi to nie jest poprawna odpowiedz")
elif mojaOdp == "B":
    print("To poprawna odpowiedź!")
elif mojaOdp == "C":
    print("Przykro mi to nie jest poprawna odpowiedz")
elif mojaOdp == "D":
    print("Przykro mi to nie jest poprawna odpowiedz")
else:
    print("Hubert: ale tu nie ma takiej odpowiedzi :) ")