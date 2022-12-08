import os, sys 

os.chdir(sys.path[0])

print("- Papuga: Jestem papugą! Gadaj do mnie:")

odp = ""
f = open("papuga.txt", "a")
while(odp != "END"):
    odp = input("- User: ")
    print("- Papuga:", odp)
    f.write(odp+"\n")

print("- Papuga: No dobra to koniec.")

f.close()
