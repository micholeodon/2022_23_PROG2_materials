import os
# pokaz na zajeciach
# potem niech sami sprobuja sobie zdebugowac ten kod


# os.path.exists 
print(os.listdir())
f = os.path.join(os.curdir, 'pierwszy.py')
d = os.path.join(os.curdir)
print("f-exist:", os.path.exists(f))
print("d-exist:", os.path.exists(d))
# os.path.isfile 
print("f-isfile:", os.path.isfile(f))
print("d-isfile:", os.path.isfile(d))

# os.path.isdir
print("f-isdir:", os.path.isdir(f))
print("d-isdir:", os.path.isdir(d))

# os.mkdir
newDir = "mojkatalog"
os.mkdir(newDir)

# os.rename
fname = "pliktestowy.txt"
f = open(fname,'w')
f.close()

os.rename(fname, "nowinka.txt") # zmiana nazwy
fname = "nowinka.txt"
os.rename(src=fname, dst=os.path.join(newDir, fname)) # przeniesienie

# skopiowanie
import shutil
shutil.copy(os.path.join(newDir,fname), "kopia.txt")
#shutil.copy2(fname, "kopia.txt")


# os.rmdir
# os.rmdir(newDir) # odkomentuj by pokazac blad

# os.remove
os.remove(os.path.join(newDir, fname))

# os.rmdir
os.rmdir(newDir)

# os.makedirs
# os.mkdir("Chorwacja/Dubrovnik") # error
os.makedirs("Chorwacja\Dubrovnik") # on Linux: makes single dir, on Win: two dirs
os.makedirs("Chorwacja/Dubrovnik") # on Linux: makes two dir, on Win: two dirs