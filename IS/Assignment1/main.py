from encryption import *

if __name__ == "__main__":
    cont = True
    while(cont):
        choice = int(input("\nWhat do you want to do?\n1. Encrypt\n2. Decrypt\nEnter Choice: "))
        if(choice == 1):
            encryptText(input("Enter the Text to be Encrypted: "))
        elif (choice == 2):
            decryptText(input("Enter the Text to be Decrypted: "))
        else:
            print("No Choice Selected")
        if input("Do you want to continue [to quit press 'q'] : ") == "q": 
            break




