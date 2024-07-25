import random
import string

charList = " " + string.punctuation + string.digits + string.ascii_letters
charList = list(charList)
key = charList.copy()
random.shuffle(key)

#Encrypt
message = input("Enter a message to encrypt: ")
eMessage = ""
keyString = ""

for letter in message:
    keyLetter = charList.index(letter)
    eMessage += key[keyLetter]

print("\nKey:")
print(keyString.join(key))
print("\nEncrypted message:\n" + eMessage)

#Decrypt
eMessage = input("\nEnter a message to decrypt: ")
message = ""
key = input("\nEnter the key: ")
key = list(key)

for letter in eMessage:
    keyLetter = key.index(letter)
    message += charList[keyLetter]

print("\nEntered Key:")
print(key) 
print("\nDecoded message: \n" + message)
