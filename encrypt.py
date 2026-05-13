from cryptography.fernet import Fernet

#this function prints without a new line for the sake of keeping prompts next to input
def printB(string):
    print(string, end='')

#determine if the user would like to use a pre-existing key and handle invalid input
printB('Do you have a key already generated that you would like to use? (y/n): ')
inp = input().lower().strip()
while (inp != 'y') and (inp != 'n'):
    print('Sorry there was a problem with your input.')
    printB('Do you have a key already generated that you would like to use? (y/n): ')
    inp = input().lower().strip()

#if the user does not have a pre-existing key, generate one for them
if inp == 'n':
    key = Fernet.generate_key()
    print(f'The following is the key which you will need to decrypt your password. Make sure to keep it in a safe place! {key.decode()}')
    
#if the user does have a pre-existing key, use it for encryption
else:
    printB('Please enter your key: ')
    key = input().strip()
cipher = Fernet(key)

#encrypt passwords until the user is done
while(True):
    printB('Please enter your password or type \'done\' to finish: ')
    inp = input().strip()
    
    #check for termination command and end program if it is found
    if inp.lower() == 'done':
        break
    
    #encrypt the password and display it for the user
    password = str.encode(inp)
    encrypted = cipher.encrypt(password)
    print(f'Here is your encrypted password: {encrypted.decode()}')
