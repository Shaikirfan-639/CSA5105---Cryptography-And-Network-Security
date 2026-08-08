{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yd1DNMZG-NAk",
        "outputId": "00e11883-262c-45e4-f395-ab3bc2015362"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Plain Text: hellooo\n",
            "Encrypted Text: ITSSGGG\n",
            "Decrypted Text: HELLOOO\n"
          ]
        }
      ],
      "source": [
        "# Monoalphabetic Substitution Cipher\n",
        "\n",
        "import string\n",
        "\n",
        "# Plaintext alphabet\n",
        "plain_alphabet = string.ascii_uppercase\n",
        "\n",
        "# Cipher alphabet (must contain all 26 unique letters)\n",
        "cipher_alphabet = \"QWERTYUIOPASDFGHJKLZXCVBNM\"\n",
        "\n",
        "# Create encryption and decryption dictionaries\n",
        "encrypt_dict = dict(zip(plain_alphabet, cipher_alphabet))\n",
        "decrypt_dict = dict(zip(cipher_alphabet, plain_alphabet))\n",
        "\n",
        "# Encryption function\n",
        "def encrypt(text):\n",
        "    text = text.upper()\n",
        "    cipher_text = \"\"\n",
        "    for ch in text:\n",
        "        if ch in encrypt_dict:\n",
        "            cipher_text += encrypt_dict[ch]\n",
        "        else:\n",
        "            cipher_text += ch\n",
        "    return cipher_text\n",
        "\n",
        "# Decryption function\n",
        "def decrypt(text):\n",
        "    text = text.upper()\n",
        "    plain_text = \"\"\n",
        "    for ch in text:\n",
        "        if ch in decrypt_dict:\n",
        "            plain_text += decrypt_dict[ch]\n",
        "        else:\n",
        "            plain_text += ch\n",
        "    return plain_text\n",
        "\n",
        "# Main Program\n",
        "message = input(\"Enter Plain Text: \")\n",
        "\n",
        "encrypted = encrypt(message)\n",
        "print(\"Encrypted Text:\", encrypted)\n",
        "\n",
        "decrypted = decrypt(encrypted)\n",
        "print(\"Decrypted Text:\", decrypted)"
      ]
    }
  ]
}



<img width="777" height="768" alt="image" src="https://github.com/user-attachments/assets/605d1688-0bbc-474d-a8c4-e9357b1aac08" />
