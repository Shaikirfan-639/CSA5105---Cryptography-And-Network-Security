# Simple Substitution Cipher - Frequency Analysis

from collections import Counter

cipher = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

# Count frequencies of symbols
freq = Counter(ch for ch in cipher if not ch.isspace())

print("Frequency Analysis:")
for symbol, count in freq.most_common():
    print(f"{symbol} : {count}")






<img width="715" height="781" alt="image" src="https://github.com/user-attachments/assets/b36c4e4f-54b9-44a6-8dc4-84540dbce4fc" />
