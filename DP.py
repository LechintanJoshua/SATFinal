def literalPur (clauze):
    aparitii = {}

    for cla in clauze:
        for lit in cla:
            aparitii[lit] = aparitii.get(lit, 0) + 1

    puri = []

    for lit in aparitii:
        if -lit not in aparitii:
            puri.append(lit)

    return puri

def gasesteUnit (clauze):
    return [cla[0] for cla in clauze if len(cla) == 1]

def eliminaLit (clauze, literal):
    clauzeNoi = []

    for cla in clauze:
        if literal in cla:
            continue

        clauzaN = [l for l in cla if l != -literal]
        clauzeNoi.append(clauzaN)

    return clauzeNoi

def rezolvaClauze (c1, c2, var):
    rez = list(set(c1 + c2))

    try:
        rez.remove(var)
    except ValueError:
        pass

    try:
        rez.remove(-var)
    except ValueError:
        pass

    return rez

def rezolva(clauze, var):
    clauze = [sorted(c) for c in clauze]
    clauzeSet = set(tuple(c) for c in clauze)
    atr = {}

    MAX_CLAUZE = 1000 
    MAX_ITERATII = 1000000

    iteratii = 0

    while iteratii < MAX_ITERATII:
        iteratii += 1
        schimbat = False

        unit = gasesteUnit(clauze)
        while unit:
            for lit in unit:
                varLit = abs(lit)
                if varLit in var:
                    var.remove(varLit)
                atr[varLit] = (lit > 0)
                clauze = eliminaLit(clauze, lit)
                schimbat = True
            unit = gasesteUnit(clauze)

        puri = literalPur(clauze)
        for lit in puri:
            varLit = abs(lit)
            if varLit in var:
                var.remove(varLit)
            atr[varLit] = (lit > 0)
            clauze = eliminaLit(clauze, lit)
            schimbat = True

        if not clauze:
            return True
        if [] in clauze:
            return False

        if not schimbat:
            if not var:
                return True

            v = var.pop(0)
            newClauze = []
            nrClauzeGenerate = 0

            posClauses = [c for c in clauze if v in c]
            negClauses = [c for c in clauze if -v in c]

            for c1 in posClauses:
                for c2 in negClauses:
                    rez = rezolvaClauze(c1, c2, v)
                    if not rez:
                        return False

                    t = tuple(sorted(set(rez)))
                    if t not in clauzeSet:
                        newClauze.append(list(t))
                        clauzeSet.add(t)
                        nrClauzeGenerate += 1

                        if nrClauzeGenerate >= MAX_CLAUZE:
                            break

            clauze += newClauze

    return False