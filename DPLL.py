from DP import literalPur, gasesteUnit, eliminaLit, rezolvaClauze

def dpll(clauze, var, max_clauze=1000, clauze_generate=0):
    while True:
        unit = gasesteUnit(clauze)
        if not unit:
            break
        for lit in unit:
            clauze = eliminaLit(clauze, lit)
            if [] in clauze:
                return False

    puri = literalPur(clauze)
    for lit in puri:
        clauze = eliminaLit(clauze, lit)
        if [] in clauze:
            return False

    if not clauze:
        return True

    frecventa = {}
    for cla in clauze:
        for lit in cla:
            frecventa[lit] = frecventa.get(lit, 0) + 1
    if not frecventa:
        return True
    lit = max(frecventa, key=frecventa.get)

    if clauze_generate >= max_clauze:
        print(f"Depășită limita de {max_clauze} clauze generate.")
        return False

    if dpll(eliminaLit(clauze, lit), var, max_clauze, clauze_generate + 1):
        return True

    if dpll(eliminaLit(clauze, -lit), var, max_clauze, clauze_generate + 1):
        return True

    return False