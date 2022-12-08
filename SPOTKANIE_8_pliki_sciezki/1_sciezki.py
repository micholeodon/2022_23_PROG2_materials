import os


# może pokaż to w terminalu a nie w Visual Code
print(os.listdir('.'))
print(os.listdir('/'))

# zmiana scieżek
print('cwd:', os.getcwd())
os.chdir('../')
print('cwd:', os.getcwd())
os.chdir('/media/')
print('cwd:', os.getcwd())

print("curdir:", os.curdir) # .
print("pardir:", os.pardir) # ..

# łączenie scieżek - NIEZALEŻNIE OD SYSTEMU
# UWAGA! os.path.join nie kontroluje poprawnosci nazw scieżek!
s = os.path.join("katalog","kolejnyKatalog","rybka","januszek.png")
print(s)
print('basename:', os.path.basename(s)) # nazwa zasobu do ktorego prowadzi sciezka
print('dirname:', os.path.dirname(s)) # sciezka w ktorej znajduje sie zasob na koncu podanej sciezki

# dobranie sie do rozszerzenia
print( os.path.splitext(s) )
ext = os.path.splitext(s)[1]
print( ext )# dobranie sie do rozszerzenia

# wykrywanie systemu
print(os.name) # 'nt' for Windows, 'posix' for Linux/UNIX, and so for MacOS as it's based os BSD

# tego raczej nie pokazuj
# if os.name == 'posix':
#     katalogRoot = '/'
# elif os.name == 'nt':
#     katalogRoot = 'C:\\'


