def fonction_1(polynome):
    position = len(polynome) - 1

    while polynome[position] == 0:
        del(polynome[position])
        position = position - 1
        if position < 0:
            break

    return polynome


def test_fonction_1():
    print(fonction_1([1, 2, 3, 4]))
    print(fonction_1([0, 1, 2, 3, 0, 4]))
    print(fonction_1([0, 1, 2, 3, 0, 4, 0, 0, 0]))
    print(fonction_1([0, 0, 0]))


def fonction_2(polynome_a, polynome_b):
    somme = []
    for a in polynome_a:
        for b in polynome_b:



def main():
    test_fonction_1()


main()
