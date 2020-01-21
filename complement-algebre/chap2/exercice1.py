def tronquer_polynomes(polynome):
    position = len(polynome) - 1
    while polynome[position] == 0:
        del (polynome[position])
        position = position - 1
        if position < 0:
            break
    return polynome


def additionner_polynomes(polynome_a, polynome_b):
    resultat = []
    for position in range(0, max(len(polynome_a), len(polynome_b))):
        tmp = 0
        if position < len(polynome_a):
            tmp += polynome_a[position]
        if position < len(polynome_b):
            tmp += polynome_b[position]
        if tmp != 0:
            resultat.append(tmp)
    return resultat


def multiplier_polynome_par_constante(polynome, constante):
    for position in range(0, len(polynome)):
        polynome[position] = polynome[position] * constante
    return [i for i in polynome if i not in [0]]


def multiplier_polynomes(polynome_a, polynome_b):
    resultat = [0] * (len(polynome_a) + len(polynome_b) - 1)
    for posA in range(0, len(polynome_a) - 1):
        for posB in range(0, len(polynome_b) - 1):
            resultat[posA+posB] += polynome_a[posA] * polynome_b[posB]
    return resultat


def main():
    print("1. TRONCATURE:")
    print(tronquer_polynomes([1, 2, 3, 4]))
    print(tronquer_polynomes([0, 1, 2, 3, 0, 4]))
    print(tronquer_polynomes([0, 1, 2, 3, 0, 4, 0, 0, 0]))
    print(tronquer_polynomes([0, 0, 0]))

    print("2. ADDITION:")
    print(additionner_polynomes([1, 2, 3, 4], [1, 2, 3, 4]))
    print(additionner_polynomes([1, 2, 3, 4], [1, 2, 3, 4, 5]))
    print(additionner_polynomes([1, 2, 3, 4, 5], [1, 2, 3, 4]))
    print(additionner_polynomes([1, 2, -3, -4], [1, 2, 3, 4]))
    print(additionner_polynomes([-1, -2, -3, -4], [1, 2, 3, 4]))
    print(additionner_polynomes([1, 2, 3, 4], []))

    print("3. MULTIPLICATION PAR UNE CONSTANTE:")
    print(multiplier_polynome_par_constante([1, 2, 3, 4], 3))
    print(multiplier_polynome_par_constante([], 1))
    print(multiplier_polynome_par_constante([1, -2, -3, -4], 3))
    print(multiplier_polynome_par_constante([1, -2, -3, -4], 0))
    print(multiplier_polynome_par_constante([1, -2, -3, -4], 0.23))


    print("4. MULTIPLICATION:")
    print(multiplier_polynomes([1, 2, 3, 4], [1, 2, 3, 4]))
    print(multiplier_polynomes())
    

main()
