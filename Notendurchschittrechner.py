
note = []

while True:     # Fügen sie ihre Noten hinzu
    Note = float(input("Welche Note wollen sie hinzufügen? "))
    note.append(Note)

    # Dies berechnet den Durchschnitt von den hinzu gefügten Noten
    summe = 0
    n = len(note)
    for Note in note: 
        summe = summe + Note
    Notendurchschnitt = summe / n

    # Der Durchschnitt der Noten wird in der Ausgabe ausgegeben
    
    print("Noten: " + str(note))
    print("Durchschnitt: " + str(Notendurchschnitt))
