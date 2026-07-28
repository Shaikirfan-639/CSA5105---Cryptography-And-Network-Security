1.Write a C program for Caesar cipher involves replacing each letter of the alphabet with the letter standing k places further down the alphabet, for k in the range 1 through 25.











text = input("Enter the text: ")
k = int(input("Enter the key (1-25): "))

if k < 1 or k > 25:
    print("Invalid key!")
else:
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            result += ch

  print("Encrypted text:", result)

  <img width="1331" height="775" alt="Screenshot 2026-07-16 110547" src="https://github.com/user-attachments/assets/97fffcf0-cbab-49fd-aeef-ffb712b9f530" />
