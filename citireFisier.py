def citesteFisier (filename):
    clauze = []
    variabile = set()

    with open (filename, 'r') as f:
        for linie in f:
            linie = linie.strip()

            if linie.startswith('c') or not linie:
                continue
            
            if linie.startswith('p'):
                continue

            literali = list(map(int, linie.split()))

            if literali and literali[-1] == 0:
                clauza = literali[:-1]
                clauze.append(clauza)

                for lit in clauza:
                    variabile.add(abs(lit))

    return clauze, variabile