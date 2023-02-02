class Bit2Dec:

    def convert(b):
        x = str(b)[::-1]
        d = 0
        nDigits = len(x)    

        for i in range(nDigits):

            if x[i] == "1":
                d += 2**i 

        return d


print(Bit2Dec.convert(10000))