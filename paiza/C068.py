N = int(input())
S = input()

alphabet = [chr(i) for i in range(65, 65+26)]
alphabet2 = alphabet[N::] + alphabet[0:N]
alphabet2_inv = alphabet[-N::] + alphabet[0:-N]

S2 = []
for i in range(len(S)):
    s_idx = alphabet.index(S[i])
    if (i+1) % 2 == 0:
        S2 += [alphabet2[s_idx]]
    else:
        S2 += [alphabet2_inv[s_idx]]
print("".join(S2))

