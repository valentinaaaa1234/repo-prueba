import multiprocessing as mp
import platform
import time

PROCESOS = 2
MB = 256
SEGUNDOS = 20

def carga(_):
    ram = bytearray(MB * 1024 * 1024)
    fin = time.time() + SEGUNDOS
    i = 0
    while time.time() < fin:
        ram[i % len(ram)] = i & 255
        i += 1

if __name__ == "__main__":
    print(f"{platform.node()} | {PROCESOS} procesos × {MB} MB | {SEGUNDOS} s")
    print("Abre htop en otra terminal")
    with mp.Pool(PROCESOS) as pool:
        pool.map(carga, range(PROCESOS))
    print("Listo")

