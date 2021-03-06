f = open("/Volumes/ExtremeSSD/Development/TRI8/IS/Assignment1/encryptionText.txt", "r")
abc = "abcdefghijklmnopqrstuvwxyz1234567890 "
encryption = f.read(37)
abcList = list(abc)
encryptionList = list(encryption)
cipherKeys = list(dict(zip(abcList, encryptionList)).keys())
cipherValues = list(dict(zip(abcList, encryptionList)).values())

#functions: monoalphabetic
def encryptText(text):
    newText = ""
    for i in text:
        for j in range(len(cipherKeys)):
            if i == cipherKeys[j]:
                newText += cipherValues[j]
    print("Encrypted Text: ", newText)

def decryptText(text):
    newText = ""
    for i in text:
        for j in range(len(cipherValues)):
            if i == cipherValues[j]:
                newText += cipherKeys[j]
    print("Decrypted Text: ", newText)

#functions: caesar cipher
def encryptTextCC(shiftKey, text):
    newText = ""
    for i in range(len(text)):
        pos = abc.index(text[i])
        key = (shiftKey + pos) % 26
        newText += abcList[key]
    print("Encrypted Text: ", newText)

def decryptTextCC(shiftKey, text):
    newText = ""
    for i in range(len(text)):
        pos = abc.index(text[i])
        key = (pos - shiftKey) % 26
        newText += abcList[key]
    print("Encrypted Text: ", newText)