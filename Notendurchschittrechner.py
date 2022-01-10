note = []

while True:     # : nicht vergessen!
    Note = float(input("Welche Note wollen sie hinzufügen? "))
    note.append(Note)

    #Notendurchschnitt ausrechnen
    summe = 0
    n = len(note)
    for Note in note: 
        summe = summe + Note
    Notendurchschnitt = summe / n

    print("Noten: " + str(note))
    print("Durchschnitt: " + str(Notendurchschnitt))
