def este_prim(n):
    """Verifică dacă un număr este prim, fără biblioteci externe."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Verificăm împărțirile doar la numere impare până la radical din n
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def gaseste_perechi_goldbach(n):
    """Găsește toate perechile de numere prime (p, q) cu p + q = n și p <= q."""
    perechi = []
    # Căutăm primul număr prim p de la 2 până la n // 2
    for p in range(2, (n // 2) + 1):
        if este_prim(p):
            q = n - p
            if este_prim(q):
                perechi.append((p, q))
    return perechi


if __name__ == "__main__":
    print("--- Verificarea Conjecturii lui Goldbach ---")
    try:
        n = int(input("Introduceți un număr natural par strict mai mare decât 2: "))

        # Validarea datelor (număr par și > 2)
        if n <= 2 or n % 2 != 0:
            print("Eroare: Numărul trebuie să fie par și strict mai mare decât 2!")
        else:
            perechi = gaseste_perechi_goldbach(n)
            print(f"\nDescompunerile pentru {n} sunt:")
            if not perechi:
                print("Nu s-au găsit perechi (caz imposibil conform conjecturii).")
            else:
                for p, q in perechi:
                    print(f"{n} = {p} + {q}")

    except ValueError:
        print("Eroare: Vreți să introduceți un număr întreg valid!")