import os, sys


print(os.getcwd())
os.chdir(sys.path[0]) # ustawia cwd na katalog, w którym jest niniejszy skrypt
print(os.getcwd())