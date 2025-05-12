from citireFisier import citesteFisier
from rezolutie import rezolutie
import time
import tracemalloc
import signal
import sys

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()



def main():
    filename = input()
    path = "./teste/"
    name = path + filename

    clauze, variabile = citesteFisier(name)

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(1000)

    tracemalloc.start()
    start = time.perf_counter()

    print("Număr de variabile:", len(variabile))
    print ("Clauze:", len(clauze))

    try:
        satisfiabil = rezolutie (clauze)
    except TimeoutException:
        print("\nTimeout: algoritmul a depaasit limita de timp.\n")
        return
    finally:
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        signal.alarm(0)

    if satisfiabil is True:
        print("\nSatisfiabil")
    elif satisfiabil is False:
        print("\nNesatisfiabil")
    else:
        print("\nFormula este NECUNOSCUTĂ (limită de clauze atinsă).")

    print(f"\nDurata execuției: {end - start:.4f} secunde")
    print(f"Memorie folosită: {current / 1024:.1f} KB (vârf: {peak / 1024:.1f} KB)")

if __name__ == "__main__":
    main()