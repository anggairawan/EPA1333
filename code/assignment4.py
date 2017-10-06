#%% 4.1
##
## The encrypt_password function.
## You can use this function in your answer.
##

import hashlib

def encrypt_password( passwd ):
    """Encrypt a plaintext password (a string). It returns the result.
    This encryption is one-way only, meaning it is not easy (impossible) to decrypt
    the encrypted password to find out the original plaintext password again."""
    return hashlib.sha256( passwd.encode() ).hexdigest()

# your code goes here

def altere_password(s):
    altered_s = s.lower()
    altered_s = altered_s.replace('i', '1')
    altered_s = altered_s.replace('a', '@')
    
    altered_s = '#'+altered_s+"!"
    altered_s = altered_s.upper()
    return altered_s

"""
s = "assignment"
altered_s = altere_password(s)
print(altered_s)
"""

fin = open("words.txt")

#hashed = "b46352779bececb48e5a8d31e58684e8da139a944715bd44f0b930f3ac46bbca"
#hashed = 'ce7a7c10b0dfd96808cca64c88cf5c5e13b7775283bdc924767887bfa32c8fa1'
#hashed = '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b'
hashed = input("Input encrypted password: ")

for line in fin:
    word = line.strip()
    pass_enc = encrypt_password(word)
    altered_pass = altere_password(word)
    alt_pass_enc = encrypt_password(altered_pass)
    #print(word, pass_enc, altered_pass, alt_pass_enc)
    
    if pass_enc == hashed:
        print("Plaintext password is: ", word)
        break
    elif alt_pass_enc == hashed:
        print("Plaintext password is: ", altered_pass)
        break
    
fin.close()
    
#%% 4.2

def create_hashed_pass_dict(file_input):
    """
    create a encrypt password : plaintext password dictionary from the word in file input
    input: text file
    output: hashed pass: word dictionary
    """
    hashed_password_dict = {}

    for line in file_input:
        word = line.strip()
        
        pass_enc = encrypt_password(word)
        
        altered_pass = alter_password(word)
        alt_pass_enc = encrypt_password(altered_pass)

        hashed_password_dict[pass_enc] = word   
        hashed_password_dict[alt_pass_enc] = altered_pass
        
    return hashed_password_dict
    
fin = open("words.txt")
hashed_dict = create_hashed_pass_dict(fin)
#test know hashed password
fin.close()
#hashed = 'b46352779bececb48e5a8d31e58684e8da139a944715bd44f0b930f3ac46bbca'
#hashed = '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b'
hashed = input("Input encrypted password:  ")

# check if the hashed password given is in dictionary
if hashed in hashed_password_dict:
    print("Plaintext password is: ", hashed_password_dict[hashed])  
else:
    print("Password cannot be found")


#%% 4.3
def print_converted_hashed_to_plain(fpass, fwords):
    # create a hashed password dictionary by using function in 4.2
    hashed_dict = create_hashed_pass_dict(fwords)

    for line in fpass:
        word = line.strip() 
        # split the username and the hashed password
        name, hashed = word.split(':')
        if hashed in hashed_dict:
            plainpass = hashed_dict[hashed]
        else:
            plainpass = "Cannot find password"

        print(name,"\t",plainpass)

# read passwordfile.txt
fpass = open("passwordfile.txt")

# read words.txt
fwords = open("words.txt")

print_converted_hashed_to_plain(fpass, fwords)
        
fpass.close()
fwords.close()
    
    
    