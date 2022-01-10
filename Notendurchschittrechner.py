
note = []

while True:
    Note = float(input("Welche Note wollen sie hinzufügen? ")) # Hier wird das Programm sie fragen, welche Note sie hinzufügen wollen
    note.append(Note)

    # Dies berechnet den Durchschnitt von den hinzugefügten Noten
    summe = 0
    n = len(note)
    for Note in note: 
        summe = summe + Note
    Notendurchschnitt = summe / n

    # Der Durchschnitt der Noten wird in der Ausgabe ausgegeben
    print("Noten: " + str(note))
    print("Durchschnitt: " + str(Notendurchschnitt))
