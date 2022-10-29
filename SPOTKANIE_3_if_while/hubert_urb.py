# MILIONERZY

pytanie = "Jaka jest stolica Polski?"

odpA = "A. Tokio"
odpB = "B. Paryż"
odpC = "C. Warszawa"
odpD = "D. Chicago"

print(pytanie)
print(odpA)
print(odpB)
print(odpC)
print(odpD)

ans = input("Podaj odpowiedź: ")
print("Powiedziałeś " + ans)

if ans == "C":
    print("To poprawna odpowiedź! Wygrywasz milion!")
elif ans == "A" or ans == "B" or ans == "D":
    print("Niepoprawna odpowiedź.")
else: 
    print("Podałeś głupoty ... :)")