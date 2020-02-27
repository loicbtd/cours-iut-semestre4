def tronquer_polynome(polynome):
    position = len(polynome) - 1
    while polynome[position] == 0:
        del (polynome[position])
        position = position - 1
        if position < 0:
            break
    return polynome


def additionner_polynomes(polynome_a, polynome_b):
    resultat = [0] * (max(len(polynome_a), len(polynome_b)))
    for position in range(0, len(resultat)):
        if position < len(polynome_a):
            resultat[position] += polynome_a[position]
        if position < len(polynome_b):
            resultat[position] += polynome_b[position]
    return resultat


def multiplier_polynome_par_constante(polynome, constante):
    for position in range(0, len(polynome)):
        polynome[position] = polynome[position] * constante
    return [i for i in polynome if i not in [0]]

# TODO: multiplier polynomes (refaire)
def multiplier_polynomes(polynome_a, polynome_b):
    resultat = [0] * (len(polynome_a) + len(polynome_b) - 1)
    for posA in range(0, len(polynome_a) - 1):
        for posB in range(0, len(polynome_b) - 1):
            resultat[posA + posB] += polynome_a[posA] * polynome_b[posB]

    resultat = tronquer_polynome(resultat)

    return resultat


def soustraire_polynomes(polynome_a, polynome_b):
    return additionner_polynomes(polynome_a, multiplier_polynome_par_constante(polynome_b, -1))


def trouver_quotient_polynomes(polynome_a, polynome_b):
    polynome_a = tronquer_polynome(polynome_a)
    polynome_b = tronquer_polynome(polynome_b)

    if len(polynome_a) < len(polynome_b):
        return []

    dividende = polynome_a
    diviseur = polynome_b
    quotient = []
    reste = []

    print("dividende = ", dividende)
    print("diviseur = ", diviseur)

    ordre_quotient = len(dividende) - len(diviseur)
    print("ordre quotient = ", ordre_quotient)

    partie_quotient = [0] * (ordre_quotient + 1)

    partie_quotient[ordre_quotient] = int(dividende[len(dividende) - 1] / diviseur[len(diviseur) - 1])

    print("partie_quotient etape 1 : ", partie_quotient)
    quotient = additionner_polynomes(quotient, partie_quotient)
    print("quotient etape 1: ", quotient)





    # quotient[ordre_quotient]

    # b = multiplier_polynomes(a, )
    # print(b)

    # partie_du_quotient = multiplier_polynomes()
    # polynome_a_soustraire = multiplier_polynomes(diviseur, )

    # soustraire_polynomes(dividende, multiplier_polynome_par_constante(polynome_b, ))

    # A - B * c = 0
    #
    # A = B * c
    # C = A / B

    # ordre = len(A) - len(B)

    #
    # while len(reste) >= len(polynome_b) or reste == 0:
    #
    #     quotient.append(reste[-1]/polynome_b[-1])
    #     reste = tronquer_polynomes(soustraire_polynomes(reste, multiplier_polynome_par_constante(polynome_b, quotient[-1])))
    #
    # return quotient


def main():
    print("1. TRONCATURE:")
    print(tronquer_polynome([1, 2, 3, 4]))
    print(tronquer_polynome([0, 1, 2, 3, 0, 4]))
    print(tronquer_polynome([0, 1, 2, 3, 0, 4, 0, 0, 0]))
    print(tronquer_polynome([0, 0, 0]))

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
    print(multiplier_polynomes([1, 1, 1, 1], [1, 1, 1, 1]))
    print(multiplier_polynomes([1, 1, 1, 1], [6]))

    print("5. QUOTIENT")
    print(trouver_quotient_polynomes([3, 0, -1, 2, 1], [-1, 1, 0, 1]))


main()
