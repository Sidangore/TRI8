from encryption import *

if __name__ == "__main__":
    cont = True
    while(cont):
        choice1 = int(input("\nWhat do you want to use?\n1. Caesar Cipher\n2. Monoalphabetic Cipher\nEnter Choice: "))
        if(choice1 == 1):
            choice2 = int(input("\nWhat do you want to do?\n1. Encrypt\n2. Decrypt Cipher\nEnter Choice: "))
            if(choice2 == 1):
                shiftKey = int(input('The shift key value: '))
                text = input("Enter the Text to be Encrypted in CC: ")
                encryptTextCC(shiftKey ,text)   
            elif(choice2 == 2):
                shiftKey = int(input('The shift key value: '))
                text = input("Enter the Text to be Decrypted in CC: ")
                decryptTextCC(shiftKey ,text) 

        elif (choice1 == 2):
            choice2 = int(input("\nWhat do you want to do?\n1. Encrypt\n2. Decrypt Cipher\nEnter Choice: "))
            if(choice2 == 1):
                encryptText(input("Enter the Text to be Encrypted: "))
            elif(choice2 == 2):
                decryptText(input("Enter the Text to be Decrypted: "))
        else:
            print("No Choice Selected")
        if input("Do you want to continue [to quit press 'q'] : ") == "q": 
            break




