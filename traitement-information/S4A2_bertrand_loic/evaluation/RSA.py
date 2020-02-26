import random
import sympy
import math


def comvertir_chaine_vers_ascii(chaine):
    return int(''.join([f'{ord(c):03}' for c in chaine]))


def ascii_vers_chaine(valeur_ascii):
    valeur_ascii_chaine = str(valeur_ascii)
    if len(valeur_ascii_chaine) % 3 != 0:
        valeur_ascii_chaine = '0' + valeur_ascii_chaine
    return ''.join(chr(int(i)) for i in [valeur_ascii_chaine[i:i + 3] for i in range(0, len(valeur_ascii_chaine), 3)])


def generer_nombre_premier_aleatoire():
    debut_plage_nombre = 10 ** 4
    fin_plage_nombres = 10 ** 5
    nombres_premiers = [i for i in range(debut_plage_nombre, fin_plage_nombres) if sympy.isprime(i)]
    return random.choice([i for i in nombres_premiers])


def bezout(a, b):
    (r, u, v, R, U, V) = (a, 1, 0, b, 0, 1)

    while R != 0:
        q = r/R
        (r, u, v, R, U, V) = (R, U, V, r - q * R, u - q * U, v - q * V)
    return r, u, v


def clef(p1, p2):
    n = p1 * p2
    c = random.randint(10, 100000)
    (r, u, v) = bezout(c, (p1 - 1) * (p2 - 1))
    d = u
    return (n, c), d


def main():
    print("main")
    random.seed(1)

    p1 = generer_nombre_premier_aleatoire()
    p2 = generer_nombre_premier_aleatoire()

    
    # print(clef(p1, p2))


main()

# def rabin_miller(n):
#     s = n - 1
#     t = 0
#     while s == 0 & 1 == 0:
#         s = s / 2
#         t += 1
#     k = 0
#     while k < 128:
#         a = random.randrange(2, n - 1)
#         v = pow(a, s, n)
#         if v != 1:
#             i = 0
#             while v != (n - 1):
#                 if i == t - 1:
#                     return False
#                 else:
#                     i = i + 1
#                     v = (v ** 2) % n
#         k += 2
#     return True
#
#
# def is_prime(n):
#     lowPrimes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
#         , 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
#         , 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269
#         , 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367
#         , 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461
#         , 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571
#         , 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661
#         , 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773
#         , 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883
#         , 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#     if n >= 3:
#         if n & 1 != 0:
#             for p in lowPrimes:
#                 if n == p:
#                     return True
#                 if n % p == 0:
#                     return False
#             return rabin_miller(n)
#     return False
#
#
# def generate_large_prime(k):
#     # k is the desired bit length
#     r = 100 * (math.log(k, 2) + 1)  # number of attempts max
#     r_ = r
#     while r > 0:
#         # randrange is mersenne twister and is completely deterministic
#         # unusable for serious crypto purposes
#         n = random.randrange(2 ** (k - 1), 2 ** (k))
#         r -= 1
#         if is_prime(n):
#             return n
#     return "Failure after " + repr(r_) + " tries."
