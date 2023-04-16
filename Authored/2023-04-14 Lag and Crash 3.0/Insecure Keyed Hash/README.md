# Insecure Keyed Hash


### Files

- [server.py](server.py)


## Description

I have created a new keyed-hash algorithm! It's faster and better than HMAC! I'll be famous!


## Intended Solution

- [script.py](script.py)

1. The signing function is simply `MD5(key|message)`.

2. The key is extremely small, it's made of 5 lower alphabetic characters.
    - This means that there's only 26^5 = 11881376 different combinations for the key.
    - This can be easily bruteforced within seconds (my laptop took less than a minute)

3. Sign a chosen plaintext `p` to get the hash value of `key + p` (let's call this `x`)

4. Bruteforce all possible hash values till the value is equals to `x`

    ```py
    # p is chosen plaintext
    # x is the hash value of key + p
    for a in asciilowercase:
        for b in asciilowercase:
            for c in asciilowercase:
                for d in asciilowercase:
                    for e in asciilowercase:
                        if md5((a+b+c+d+e+p).encode()).hexdigest() == x:
                            print(a+b+c+d+e)
                            # To stop it use Ctrl+C or something else lmao
    ```

    ```py
    # Recursive version of solution cuz I was bored
    def get_key(x: str, p: bytes, k=b"", depth=5):
        if depth:
            for i in ascii_lowercase:
                result = get_key(x, p, k+i.encode(), depth=depth-1)
                if result:
                    break
            return result
        elif md5(k+p).hexdigest() == x:
            return k
    ```

5. After getting the key, sign the `"Better than HMAC!"` message manually and pass the value to verify message

6. If the message `"Better than HMAC!.<hash>"` is verified, the player should receive the flag


## Flag

`LNC2023{H0w?_1t_5hoU1d_h4v3_be3n_5tr0ng3r_7h4N_HMAC_QAQ!}`
