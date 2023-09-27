# Ali Ramazani
# Credit: Cole explained how the 2 byte blocks work. Armira helped me figure out how to find d.

import math
# Given information
g, p = 7, 61
A, B = 30, 17

#Find X and Y
for X in range(0, p):
    if A == (g ** X) % p:
        print("X: ", X, " and shared secret: ", (B ** X) % p)
        break
            
for Y in range(0, p):
    if B == (g ** Y) % p:
        print("Y: ", Y, " and shared secret: ", (A ** Y) % p)
        break
    
'''
1. Figure out the shared secret agreed upon by Alice and Bob. This will be an integer.
    - X:  41  and shared secret:  6
    - Y:  23  and shared secret:  6
2. Show your work. Exactly how did you figure out the shared secret?
    - I used the two loops above to find the values of X and Y by brute force and used to find the shared secret.
3. Show precisely where in your process you would have failed if the integers involved were much larger.
    - The brute force approach would be very inefficient. This approach relies on iterating through all possible values of X and Y within the range [0, p) until a match is found. 
       As p gets larger, the number of iterations required to find a match increases significantly.
'''

e, n = 17, 170171

ciphers = [65426, 79042, 53889, 42039, 49636, 66493, 41225, 58964,
126715, 67136, 146654, 30668, 159166, 75253, 123703, 138090,
118085, 120912, 117757, 145306, 10450, 135932, 152073, 141695,
42039, 137851, 44057, 16497, 100682, 12397, 92727, 127363,
146760, 5303, 98195, 26070, 110936, 115638, 105827, 152109,
79912, 74036, 26139, 64501, 71977, 128923, 106333, 126715,
111017, 165562, 157545, 149327, 60143, 117253, 21997, 135322,
19408, 36348, 103851, 139973, 35671, 93761, 11423, 41336,
36348, 41336, 156366, 140818, 156366, 93166, 128570, 19681,
26139, 39292, 114290, 19681, 149668, 70117, 163780, 73933,
154421, 156366, 126548, 87726, 41418, 87726, 3486, 151413,
26421, 99611, 157545, 101582, 100345, 60758, 92790, 13012,
100704, 107995]


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


# Finding p and q
p = 2
while p < n:
    if n % p == 0 and is_prime(p):
        q = n // p
        if is_prime(q):
            break
    p += 1

if p < n:
    print("p =", p)
    print("q =", q)
    print("n =", n)
else:
    print("No suitable p and q found for n =", n)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

lamda_n = lcm(p - 1, q - 1)

def d_finder():
    for d in range(1000000):
            if (e * d) % lamda_n == 1:
                return d
d = d_finder()


ciphers = [65426, 79042, 53889, 42039, 49636, 66493, 41225, 58964,
126715, 67136, 146654, 30668, 159166, 75253, 123703, 138090,
118085, 120912, 117757, 145306, 10450, 135932, 152073, 141695,
42039, 137851, 44057, 16497, 100682, 12397, 92727, 127363,
146760, 5303, 98195, 26070, 110936, 115638, 105827, 152109,
79912, 74036, 26139, 64501, 71977, 128923, 106333, 126715,
111017, 165562, 157545, 149327, 60143, 117253, 21997, 135322,
19408, 36348, 103851, 139973, 35671, 93761, 11423, 41336,
36348, 41336, 156366, 140818, 156366, 93166, 128570, 19681,
26139, 39292, 114290, 19681, 149668, 70117, 163780, 73933,
154421, 156366, 126548, 87726, 41418, 87726, 3486, 151413,
26421, 99611, 157545, 101582, 100345, 60758, 92790, 13012,
100704, 107995]


decrypted_blocks = []
for c in ciphers:
    decrypted_blocks.append((c ** d) % n)
    

# Function to convert a 2-byte block to ASCII characters
def bytes_to_ascii(block):
    return chr((block >> 8) & 0xFF) + chr(block & 0xFF)

# Convert decrypted blocks to ASCII characters
decrypted_message = ''
for block in decrypted_blocks:
    decrypted_message += (bytes_to_ascii(block))


print(decrypted_message)

'''

1. Figure out the encrypted message sent from Alice to Bob.
    - Hi Bob. I'm walking from now on. Your pal, Alice. 
      https://foundation.mozilla.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/
2. Show your work:
    - Alice used Bob's public key to encode the message -> x^eB mod nB, where x represent the ascii value of character in the message.
    - I used pyton code to show my work.
3. Show precisely where in your process you would have failed if the integers involved were much larger.
    - if p and q were much larger, then it would take extremely long time to find them using the brute force approach that I did.
4. Explain, briefly, why the message encoding Alice used would be insecure even if Bob's keys involved larger integers.
    - Alice encoded each character one by one which is simply a substitute cipher that can easily be broken using letter frequency and a dictionary. 
'''