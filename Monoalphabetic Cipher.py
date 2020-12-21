plain = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
cipher = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
          'V', 'B', 'N', 'M']

msg = input("Enter Message: ")

# Encyption Code
Q = ''
E = [0] * len(msg)
for i in range(len(plain)):
    for j in range(len(msg)):
        if msg[j] == plain[i]:
            E[j] = cipher[i]

enc = Q.join(E)
print('Encyption: ' + enc)

# Decryption Code
dec = ""
D = [0] * len(enc)
for l in range(len(cipher)):
    for m in range(len(enc)):
        if enc[m] == cipher[l]:
            D[m] = plain[l]

print('Decyption: ' + dec.join(D))
