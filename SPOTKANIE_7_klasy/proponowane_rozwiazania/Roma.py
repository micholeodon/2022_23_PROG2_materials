# Zaprojektuj klasę przyjmującą liczbę całkowitą z zakresu 1-20 
# i zamieniająca je na liczbę zapisaną cyframi rzymskimi.


class RomanConverter:

    isNotValidNumber = False

    # konstruktor
    def __init__(self, num):
        self.rawNumber = num
        self.convertedNumber = None

        # sprawdzam czy liczba z zakresu 1-20
        if (not isinstance(num, int)) or  (num > 20) or (num < 1):
            RomanConverter.isNotValidNumber = True    
            
        
    def convertFromArabicToRoman(self):

        x = self.rawNumber
        if RomanConverter.isNotValidNumber is True:
            print("ERROR! You can convert only natural numbers 1-20!")
        else:
            y = ""
            d = {10: "X", 9: "IX", 5:"V", 4:"IV", 1:"I"}

            for i in d.keys(): 
                r = x // i
                x = x - r*i
                y = y + r*d[i]

            self.convertedNumber = y


x = 20
machina = RomanConverter(x)
print(machina.rawNumber)
machina.convertFromArabicToRoman()
print(machina.convertedNumber)