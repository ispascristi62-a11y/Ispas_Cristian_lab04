import os


def citeste_numere_fisier(nume_fisier):
    """Citește două numere mari din fișier, câte unul pe linie,

    verificând existența și validitatea lor.
    """
    if not os.path.exists(nume_fisier):
        print(f"Eroare: Fișierul '{nume_fisier}' nu există!")
        return None, None

    with open(nume_fisier, "r", encoding="utf-8") as f:
        linii = [linie.strip() for linie in f.readlines() if linie.strip()]

    if len(linii) < 2:
        print(
            "Eroare: Fișierul trebuie să conțină cel puțin două numere (câte unul pe"
            " linie)!"
        )
        return None, None

    numar1 = linii[0]
    numar2 = linii[1]

    # Validare că sunt formate doar din cifre
    if not numar1.isdigit() or not numar2.isdigit():
        print("Eroare: Numerele din fișier trebuie să conțină doar cifre!")
        return None, None

    return numar1, numar2


def aduna_numere_mari(s1, s2):
    """Adună două numere mari reprezentate ca șiruri de caractere,

    de la dreapta la stânga, folosind transportul.
    """
    s1 = s1.lstrip("0") or "0"
    s2 = s2.lstrip("0") or "0"

    i = len(s1) - 1
    j = len(s2) - 1
    transport = 0
    rezultat = []

    while i >= 0 or j >= 0 or transport > 0:
        cifra1 = int(s1[i]) if i >= 0 else 0
        cifra2 = int(s2[j]) if j >= 0 else 0

        suma = cifra1 + cifra2 + transport
        transport = suma // 10
        cifra_curenta = suma % 10
        rezultat.append(str(cifra_curenta))

        i -= 1
        j -= 1

    rezultat.reverse()
    return "".join(rezultat)


def inmulteste_numere_mari(s1, s2):
    """Înmulțește două numere mari prin produse parțiale și transport

    (metoda înmulțirii în coloană).
    """
    s1 = s1.lstrip("0") or "0"
    s2 = s2.lstrip("0") or "0"

    if s1 == "0" or s2 == "0":
        return "0"

    n = len(s1)
    m = len(s2)
    res = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            produs = int(s1[i]) * int(s2[j])
            suma = produs + res[i + j + 1]

            res[i + j + 1] = suma % 10
            res[i + j] += suma // 10

    rezultat_str = "".join(map(str, res))
    rezultat_str = rezultat_str.lstrip("0")

    return rezultat_str if rezultat_str else "0"


if __name__ == "__main__":
    print("--- Adunarea și Înmulțirea Numerelor Mari ---")
    nume_fisier = "numere.txt"

    s1, s2 = citeste_numere_fisier(nume_fisier)

    if s1 and s2:
        print(f"Numărul 1 citit: {s1}")
        print(f"Numărul 2 citit: {s2}")

        suma = aduna_numere_mari(s1, s2)
        produs = inmulteste_numere_mari(s1, s2)

        print(f"\nRezultate:")
        print(f"Suma   = {suma}")
        print(f"Produs = {produs}")