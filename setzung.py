
def inputt():
    x = input("Welche Noten Möchtest du ändern? Mathe(1); Physik(2); Deutsch(3); Englisch(4); Gesamtschnitt(5); Exit(6): ")
    if x == "1":
        Mathe()
    elif x == "2":
        Physik()
    elif x == "3":
        Deutsch()
    elif x == "4":
        Englisch()
    elif x == "5":
        Gesamtschnitt()
    elif x == "6":
        exit
    
def Mathe():
    with open("Mathe.txt","w") as myFile:
        mathe_note1 = input("1. HJ Note: ")
        myFile.write(mathe_note1 + "\n")
        mathe_note2 = input("2. HJ Note: ")
        myFile.write(mathe_note2 + "\n")
        mathe_note3 = input("3. HJ Note: ")
        myFile.write(mathe_note3 + "\n")
        mathe_note4 = input("4. HJ Note: ")
        myFile.write(mathe_note4 + "\n")
        mathe_note5 = input("Abschlussprüfungs Note: ")
        myFile.write(mathe_note5 + "\n")
    inputt()
def Physik():
    with open("Physik.txt","w") as myFile:
        Physik_note1 = input("1. HJ Note: ")
        myFile.write(Physik_note1 + "\n")
        Physik_note2 = input("2. HJ Note: ")
        myFile.write(Physik_note2 + "\n")
        Physik_note3 = input("3. HJ Note: ")
        myFile.write(Physik_note3 + "\n")
        Physik_note4 = input("4. HJ Note: ")
        myFile.write(Physik_note4 + "\n")
    inputt()
def Deutsch():
    with open("Deutsch.txt","w") as myFile:
        Deutsch_note1 = input("1. HJ Note: ")
        myFile.write(Deutsch_note1 + "\n")
        Deutsch_note2 = input("2. HJ Note: ")
        myFile.write(Deutsch_note2 + "\n")
        Deutsch_note3 = input("3. HJ Note: ")
        myFile.write(Deutsch_note3 + "\n")
        Deutsch_note4 = input("4. HJ Note: ")
        myFile.write(Deutsch_note4 + "\n")
        Deutsch_note5 = input("Abschlussprüfungs Note: ")
        myFile.write(Deutsch_note5 + "\n")
    inputt()
def Englisch():
    with open("Englisch.txt","w") as myFile:
        Englisch_note1 = input("1. HJ Note: ")
        myFile.write(Englisch_note1 + "\n")
        Englisch_note2 = input("2. HJ Note: ")
        myFile.write(Englisch_note2 + "\n")
        Englisch_note3 = input("3. HJ Note: ")
        myFile.write(Englisch_note3 + "\n")
        Englisch_note4 = input("4. HJ Note: ")
        myFile.write(Englisch_note4 + "\n")
    inputt()
def Gesamtschnitt():
    with open("Gesamtschnitt.txt","w") as myFile:
        Gesamtschnitt = input("Gesammtschnitt: ")
        myFile.write(Gesamtschnitt)
    inputt()

inputt()

