def freqOfNumbers(lista):

    sprawdzone = []
    for x in lista:
        if x in sprawdzone:
            continue
        
        print(str(x) + ' : ' + str(lista.count(x)))
        sprawdzone.append(x)
        

listucha = [1,2,3,2,2.23,3,-1,6,5,2.23]
freqOfNumbers(listucha)

