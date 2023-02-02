import os, numpy

def getSubjectsDataFromFile(filePath):

    allRowsNoHeader = []
    with open(filePath, 'r') as file:
        headerRow = file.readline()

        for row in file:
            row = row.strip() # remove ending \n
            list = row.split(sep = ",")
            allRowsNoHeader.append(list)

    return allRowsNoHeader

def getSubjectCode(row):
    name = row[1]
    surname = row[0]
    year = row[2]

    code = surname[0:2].upper() + name[0:2].upper() + year[-3] + year[-2] + year[-1]
    return code

# checking where is the medical_data.csv file
print(os.listdir('../'))

# read file
filePath = os.path.join('..', 'badani.csv')

# process data
allRowsNoHeader = getSubjectsDataFromFile(filePath)
print(allRowsNoHeader)

for row in allRowsNoHeader:
    subjCode = getSubjectCode(row)
    print(subjCode)
    if(not os.path.exists(subjCode)): 
        os.mkdir(subjCode)