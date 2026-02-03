def texte(a):
    a = a.lower()
    mot = a.split()
    
    print("Nombre de mots :", len(mot))
    pluslong = ""
    total_v = 0
    voyelles = "aeiouy"
    for m in mot:
        if len(m) > len(pluslong):
            pluslong = m
            
    for lettre in a:
        if lettre in voyelles:
            total_v = total_v + 1
            
    print(" le plus long mot est :", pluslong)
    print("Total voyelles :", total_v)
    resul = []
    for m in mot:
        if len(m) % 2 == 0:
            resul.append(m.upper())
        else:
            resul.append(m)
            
    print("Phrase finale :", " ".join(resul))
entree = input("Entrez votre phrase : ")
texte(entree)