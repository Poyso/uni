# 2 numeri primi
p, q = 17, 29
n = p*q
phi = (p-1)*(q-1)
e = 5  # (e, phi(n))=1


def extended_gdc(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return old_r, old_s, old_t
    # resto, la x, la y


d = phi + extended_gdc(phi, e)[2]
inversa_d = d % phi
inversa_e = e % phi
print("Inversa d ", inversa_d)
print("Inverssa e ", inversa_e)
# pubblichiamo "n" ed "e"
# teniamo segreti "p","q" e "d"

m = 89  # il messagio da criptare e decriptare

crypted_m = m ** e % n
print(crypted_m)
decrypted_m = m ** d % n
print(crypted_m)
