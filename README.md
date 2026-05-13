# Post-Mortem_Password_Recovery
## DISCLAIMER: ALTHOUGH MORE SAFE THAN STORING PLAINTEXT PASSWORDS, THS IS STILL NOT IMMUNE TO BEING HACKED!

This project is a proof of concept of an application that would have the aim of post mortem recovery of passwords, or the basis for a password manager. As I am not a digital cryptography expert, I would advise against using this code for anything other than educational purposes.

## HOW TO USE:
`encrypt.py`

Run encrypt.py and follow the instructions to receive password key and encrypted passwords. When entering plain text passwords, you may also include associated information if you choose to, in order to remove storing the context in plain text. For example, when prompted for a password you may input 'gmail: example@gmail.com password: password'. Then when using decrypt.py the given context will be displayed (as long as you provide the correct key and encrypted password).

`decrypt.py`

Run decrypt.py and provide your key and encrypted passwords for them to be decrypted into plain text.
