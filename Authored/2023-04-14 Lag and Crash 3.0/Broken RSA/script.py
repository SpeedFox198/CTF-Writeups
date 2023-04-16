from Crypto.Util.number import long_to_bytes
from math import gcd


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)

    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y


p = 12745443776097937486523731981184244411822246670344825081786250598280592311994645818017369055015305576625489048312376829887862697232698960303123727339439477
q = 6965691623673764963283701881605906791484292250300568740181083332830802480178930748628555885283810920150672372660644966641894191414330596203094237460731853
c = 51246606178817027144048790384294344409078205278660263649138314308484271379271492418276059836372460273067275885546317401508060728580046016291398622205239294202483332638706880399609813252751351178753076424449513521022597436767316972137030942140105737604756013333385824335007108113055833516556345445260667314569
e = 1616
n = p * q

phi = (p-1) * (q-1)
x = gcd(phi, e)
# print(x)
d = pow(e//x, -1, phi)
y = pow(c, d, n)


def get_candidates(k, N, candidates:list=None, power=1):
    if not candidates:
        candidates = [k]

    for i in range(len(candidates)):
        candidates[i] = modular_sqrt(candidates[i], N)
        candidates.append(N - candidates[i])

    power -= 1

    if power > 0:
        return get_candidates(k, N, candidates=candidates, power=power)
    else:
        return candidates

candidates_1 = get_candidates(y, p, power=4)
candidates_2 = get_candidates(y, q, power=4)

m1, m2 = gcdExtended(p, q)[1:]

possible_flags = []

for a1 in candidates_1:
    for a2 in candidates_2:
        possible_flags.append((a1*m2*q + a2*m1*p) % n)

for i in possible_flags:
    flag = long_to_bytes(i)
    if b"LNC2023" in flag:
        print(flag.decode())
