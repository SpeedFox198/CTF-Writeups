# Broken RSA


### Files

- [challenge.py](challenge.py)
- [output.txt](output.txt)


## Challenge Description

My friend had a secret message for me.
However, he made a mistake when encrypting the message, and now I am unable to decrypt it!
Could you decrypt and recover the message for me?


## Intended Solution

- [script.py](script.py)

1. Terms:
    - `p` - Prime number p used in RSA
    - `q` - Prime number q used in RSA
    - `n` - Modulus number used in RSA (`n = p * q`)
    - `phi` - Euler's totient (go search it up)
    - `e` - Public exponent
    - `m` - Message (plaintext message, contains the flag)
    - `c` - Ciphertext (encryted version of message, decrypt this to get flag)
    - `^` - Symbol for exponent (`a^b` means `a` raised to the power of `b`)
    - `≡` - Symbol for congruence (used in modular arithmetic)
    - `(mod n)` - ([Go look up on Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence))
    - GCD - Greatest common divisor
    - CRT - Chinese remainder theorem

2. Players would need to recognise that:
    - The message is encrypted similarly to in RSA.
    - However, the `e` public exponent is a composite number.
    - This means that a coresponding `d` value can't be calculated

3. Let's simplify the equation, we can first find the GCD of `e` and `phi`:  
    Python:
    ```py
    phi = (p-1) * (q-1)
    x = gcd(phi, e)
    print(x)  # x = 16
    ```

4. Since `x = 16` let's continue to simplify the equation:  
    Math:
    ```math :D
    e = 1616
      = 11 * 16

    c ≡ m^e (mod n)
    c ≡ (m^16)^11 (mod n)
    c ≡ M^11 (mod n)  (Let M = m^16)
    ```

5. Since 11 is a prime number, it is coprime to `phi`, this means that we can find a corresponding private exponent `d` and decode it like in RSA:  
    More python:
    ```py
    # btw e//x == 11
    d = pow(e//x, -1, phi)  # d is inverse of e
    y = pow(c, d, n)  # Decrypt c to y
    ```
    More math:
    ```more math :)
    c ≡ M^11 (mod n)
    M ≡ c^d (mod n)
    M ≡ y (mod n)
    y ≡ M (mod n)
    y ≡ m^16 (mod n)
    ```

6. Player will need to know that 16 is a power of 2 and that something called modular square root exists:  
    Even more maths:
    ```even more math :/
    y ≡ m^16 (mod n)
    y ≡ m^(2^4) (mod n)
    ```
    Simply put, modular square root of `y` 4 times would give us `m`

7. Read up on [modular square root](https://www.rieselprime.de/ziki/Modular_square_root) (jokes)

8. So modular square root works if the modulus is a prime number
    - Since `n = p * q` we do modulus of `p` or `q` instead
    - Modular square root of `y` will result in +- square root of `y`
    - This means that we have to do the 2nd modular square root on positive square root of `y` and negative square root of `y`

9. Get any `modular_sqrt` function from [online](https://gist.github.com/nakov/60d62bdf4067ea72b7832ce9f71ae079) and find all possible 16th roots of `y`:
    ```py
    # A recursive solution that is elagant :)
    # Stores the possible roots in cadidates list
    # k is the value to square root, N is the modulo
    # power is the number of times to square root
    # Returns a list of possible square root values
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

    candidates_1 = get_candidates(y, p, power=4)  # Possible candidates with modulo p
    candidates_2 = get_candidates(y, q, power=4)  # Possible candidates with modulo q
    ```

10. Since we used modulo `p` and `q`
    - If `m` is smaller than `p` or `q` we would have decrypted the message already.
    - However ~~I am evil~~ `m` is larger than both `p` and `q`
    - This means that we have to use CRT to find the possible values of `m`

11. Get any `gcdExtended` function from [online](https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/) and use CRT to find all possible values of `m`:
    ```py
    # The m here is using the conventional naming of variables in CRT
    m1, m2 = gcdExtended(p, q)[1:]
    possible_flags = []  # Stores the possible m

    # Go through both possible list of values and use CRT to calculate value of possible m
    for a1 in candidates_1:
        for a2 in candidates_2:
            possible_flags.append((a1*m2*q + a2*m1*p) % n)

    # Loop through and find the message
    for i in possible_flags:
        flag = long_to_bytes(i)
        if b"LNC2023" in flag:
            print(flag.decode())  # Print message when found
    ```

12. The decode message containing the flag should be printed:
    ```
    So as I was saying LNC2023{Th1s_i5_wHy_e_h45_t0_B3_c0pR1m3_T0_phi}
    ```


## Flag

`LNC2023{Th1s_i5_wHy_e_h45_t0_B3_c0pR1m3_T0_phi}`
