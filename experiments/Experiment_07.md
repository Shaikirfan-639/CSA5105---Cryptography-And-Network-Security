# Simple Substitution Cipher Decryption (Gold-Bug Cipher)

cipher = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

# Substitution table obtained from frequency analysis
mapping = {
    '5':'A',
    '3':'G',
    '‡':'O',
    '†':'D',
    '0':'L',
    ')':'S',
    '6':'I',
    '*':'N',
    ';':'T',
    '4':'H',
    '8':'E',
    '2':'B',
    '.':'P',
    '¶':'V',
    ']':'C',
    ':':'R',
    '(':'F',
    '?':'Y',
    '1':'M',
    '9':'U',
    '—':'W'
}

plaintext = ""

for ch in cipher:
    if ch in mapping:
        plaintext += mapping[ch]
    else:
        plaintext += ch

print("Decrypted Message:\n")
print(plaintext)





<img width="725" height="587" alt="image" src="https://github.com/user-attachments/assets/4bd3336f-d642-46c8-8772-408ef7ae4285" />
