
with open("Mathe.txt", "r") as myFile:
    mathe = myFile.readlines()
with open("Physik.txt", "r") as myFile:
    Physik = myFile.readlines()
with open("Deutsch.txt", "r") as myFile:
    Deutsch = myFile.readlines()
with open("Englisch.txt", "r") as myFile:
    Englisch = myFile.readlines()
with open("Gesamtschnitt.txt", "r") as myFile:
    Gesamt = myFile.read()


m = 3*(int(mathe[0]) + int(mathe[1]) + int(mathe[2]) + int(mathe[3]) + int(mathe[4]))
p = 2*(int(Physik[0]) + int(Physik[1]) + int(Physik[2]) + int(Physik[3]))
d = int(Deutsch[0]) + int(Deutsch[1]) + int(Deutsch[2]) + int(Deutsch[3]) + int(Deutsch[4]) 
e = int(Englisch[0]) +  int(Englisch[1]) + int(Englisch[2]) + int(Englisch[3]) 


y = 10 + 6*((m + p + d + e)/32)
x = 120-20*(float(Gesamt[0]) + float(Gesamt[2])/10)


z = 0.65 * x + 0.35* y 

print("\nDie ereichte Punktzahl ist:   "+ str(z)+"\n")

if 73 <= z <= 83:     
    print("\nIm Test muss mindestens die Punktezahl   " + str(int((((70-0.5*int(x))/0.5)-10)/(6))+1) + "   ereicht werden\n")

elif z < 73:
    print("Damn bro du hast verkackt!")
else:
    print("GG")
