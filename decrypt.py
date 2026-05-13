from cryptography.fernet import Fernet

#this function prints without a new line for the sake of keeping prompts next to input
def printB(string):
    print(string, end='')

#prompts the user for the key used to encrypt their password(s)
printB('Please enter your key: ')
key = input().strip()
cipher = Fernet(key)

#decrypt passwords until the user is done
while(True):
    printB('Please enter your encrypted password or type \'done\' to finish: ')
    inp = input().strip()
    
    #check for termination command and end program if it is found
    if inp.lower() == 'done':
        break
    
    #todo: change
    #encrypt the password and display it for the user
    password = str.encode(inp)
    decrypted = cipher.decrypt(password)
    print(f'Here is your decrypted password: {decrypted.decode()}')

