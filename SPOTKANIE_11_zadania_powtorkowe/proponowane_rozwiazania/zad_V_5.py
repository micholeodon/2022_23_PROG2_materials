import os, numpy

def getSubjectsDataFromFile(filePath):

    allRowsNoHeader = []
    with open(filePath, 'r') as file:
        headerRow = file.readline()

        for row in file:
            row = row.strip() # remove ending \n
            list = row.split(sep = " ")
            allRowsNoHeader.append(list)

    return allRowsNoHeader


def countBMI(height, mass):
    # height in m
    # mass in kg
    h_meters = height/100
    return mass/(h_meters*h_meters)


def showDataWithBMI(dataRows):

    for subjectData in dataRows:
        name    = subjectData[0]
        surname = subjectData[1]
        age     = int(subjectData[2])
        height  = float(subjectData[3])
        mass    = float(subjectData[4])

        BMI     = countBMI(height, mass)
        warn    = ""
        if BMI < 18.5 or BMI > 24.9:
            warn = " !!! "

        print(f"{name} {surname} {BMI} {warn}")
        
def showDataRows(dataRows):
    for row in dataRows:
        for el in row:
            print(el, end=" ")

        print()

def sortRowsByWeight(dataRows):

    masses = []
    for subjectData in dataRows:
        mass    = float(subjectData[4])    
        masses.append(mass)

    idx = numpy.argsort(masses)

    sortedRows = []
    for i in idx:
        sortedRows.append(dataRows[i])

    return sortedRows

def sortRowsBySurname(dataRows):

    surnames = []
    for subjectData in dataRows:
        surname    = subjectData[1]
        surnames.append(surname)

    idx = numpy.argsort(surnames)

    sortedRows = []
    for i in idx:
        sortedRows.append(dataRows[i])

    return sortedRows


def averageHeightOlderThan(age, dataRows):
    
    sumH = 0  
    for subjectData in dataRows:
        age     = int(subjectData[2])
        height  = float(subjectData[3])

        if age > 30:
            sumH += height 

    n = len(dataRows)
    avg = sumH/n

    return avg

# checking where is the medical_data.csv file
print(os.listdir('../'))

# read file
filePath = os.path.join('..', 'medical_data.csv')

# process data
allRowsNoHeader = getSubjectsDataFromFile(filePath)
print(allRowsNoHeader)

print("Tabela uzupełniona o BMI")
showDataWithBMI(allRowsNoHeader)

print("\nTabela posortowana wg wagi:")
showDataRows(sortRowsByWeight(allRowsNoHeader))

print("\nTabela posortowana wg nazwisk: ")
showDataRows(sortRowsBySurname(allRowsNoHeader))

avg = averageHeightOlderThan(age = 30, dataRows = allRowsNoHeader)
print(f"Średni wzrost dla osób powyżej 30 roku życia: {avg}")