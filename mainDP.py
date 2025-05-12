from citireFisier import citesteFisier
from DP import rezolva
import time
import tracemalloc
import signal
import sys

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def main():
    filename = input();
    path = "./teste/"
    name = path+filename

    clauze, variabile = citesteFisier(name)
    variabile = sorted(list(variabile))

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(1000)

    tracemalloc.start()
    start = time.perf_counter()

    print("Număr de variabile:", len(variabile))
    print("Număr de clauze:", len(clauze))

    try:
        satisfiabil = rezolva(clauze, variabile)
    except TimeoutException:
        print("\nTimeout: algoritmul a depășit limita de timp.\n")
        return
    finally:
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        signal.alarm(0)

    if satisfiabil:
        print("\nSAT")
    else:
        print("\nUNSAT")

    print(f"\nDurata execuției: {end - start:.4f} secunde")
    print(f"Memorie folosită: {current / 1024:.1f} KB (vârf: {peak / 1024:.1f} KB)")

if __name__ == "__main__":
    main()