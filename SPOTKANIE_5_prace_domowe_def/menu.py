parametry = {
    "jasność": 50,
    "kontrast" : 50,
    "bluetooth" : False,
}

def ustawJasność():
    parametry["jasność"] = int(input("Podaj jasność: "))
    print(f"Jasność: {parametry['jasność']}")

def ustawKontrast():
    parametry["kontrast"] = int(input("Podaj kontrast: "))
    print(f"Kontrast: {parametry['kontrast']}")


def przełączBluetooth():
    if(parametry["bluetooth"] == True):
        parametry["bluetooth"] = False
        print("Bluetooth: WYŁĄCZONE")
    else:
        parametry["bluetooth"] = True 
        print("Bluetooth: WŁĄCZONE")


def wyświetlMenu(listaOpcji, endText):
    opt = ""

    while(opt != endText):
        
        i = 1
        for o in listaOpcji.keys():
            print(f"{i} - {o}")
            i += 1

        ans = input("Wybierz opcję: ")
        
        opcje = list(listaOpcji.keys())
        opt = opcje[int(ans)-1]

        if(opt != endText):
            listaOpcji[opt]()


def menuGłówne():

    listaOpcji = {
        "Opcje obrazu": menuOpcjeObrazu,
        "Włącz/wyłącz Bluetooth": przełączBluetooth, 
        "Koniec": None}

    wyświetlMenu(listaOpcji=listaOpcji, endText="Koniec")

def  menuOpcjeObrazu():

    listaOpcji = {
        "Ustaw jasność": ustawJasność,
        "Ustaw kontrast": ustawKontrast, 
        "Powrót": None}

    wyświetlMenu(listaOpcji=listaOpcji, endText = "Powrót")
   


menuGłówne()
