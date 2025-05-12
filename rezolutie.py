def rezolva (clauza1, clauza2, pivot):
    rezultat = []

    for lit in clauza1:
        if lit != pivot:
            rezultat.append(lit)

    for lit in clauza2:
        if lit != -pivot:
            rezultat.append(lit)

    rezultat = list(set(rezultat))

    rezultat.sort(key=lambda x: (abs(x), x))

    return rezultat

def esteClauzaNoua (clauza, cunoscute):
    return frozenset(clauza) not in cunoscute

def rezolutie (clauze, pragMax = 10_000_000):
    cunoscute = set(frozenset(cl) for cl in clauze)
    clauzeNoi = set()
    total = 0

    while True:
        perechi = [(ci, cj) for i, ci in enumerate(clauze) for cj in clauze[i+1:]]

        for cl1, cl2 in perechi:
            for lit in cl1:
                if -lit in cl2:
                    rezolventa = rezolva(cl1, cl2, lit)

                    if not rezolventa:
                        return False
                    
                    rezSet = frozenset(rezolventa)

                    if rezSet not in cunoscute and rezSet not in clauzeNoi:
                        clauzeNoi.add(rezSet)
                        total += 1

                    if total > pragMax:
                        return "necunoscut"
        
        if not clauzeNoi:
            return True
        
        for cl in clauzeNoi:
            clauze.append(list(cl))
            cunoscute.add(cl)

        clauzeNoi.clear()