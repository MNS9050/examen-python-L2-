students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7)
]
def calcul(maliste):
    somme = 0
    notes = []
    for nom, note in maliste:
        somme += note
        notes.append(note)
    
    moyenne = somme / len(maliste)
    return moyenne, max(notes), min(notes)
def repartition(maliste):
    admis = []
    ajournes = []
    nomsadmis = []
    
    for nom, note in maliste:
        if note >= 10:
            admis.append((nom, note))
            nomsadmis.append(nom)
        else:
            ajournes.append((nom, note))
    nomsadmis.sort()
    return admis, ajournes, nomsadmis
print("Liste des étudiants et leurs notes :", students)
moy, note_max, note_min = calcul(students)
print(f"la moyenne de la classe : {moy}")
print(f"la note maximal est : {note_max}")
print(f"la note minimal c'est : {note_min}")
admis, ajournes, noms_admis_tries = repartition(students)
print("etudiants admis :", admis)
print("etudiants ajournés :", ajournes)
