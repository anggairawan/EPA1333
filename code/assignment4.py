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

secret_encrypted = encrypt_password("secret")

"""
Hacking (finding) the passwords
Unfortunately, some users use passwords that are simply existing words or simple variations on them. A simple variations on words are to:
replace each instance of the letters i and I (small and capital i) with the number 1 (one)
replace each instance of the letters a and A (small and capital a) with the character @
add a hash sign (#) at the beginning of the word
add an exclamation mark (!) at the end of the word
capitalize all letters

For example, a user might use the password "#@SS1GNMENT!" which is a variation on the word "assignment".
You are going to write a program that uses a file containing a long list of possible passwords to try to find the plaintext passwords of users given a password file with encrypted passwords.
Hint: Make sure to break up your code in smaller parts (functions) and to first think about the solution (use paper!) before you start coding!
Hint: You may assume that a user either uses a word unaltered from the words file as a password or uses all 5 ways to alter an existing word from the file simultaneously as a password (so either "assignment" or "#@SS1GNMENT!").
Hint: You can use the provided The encrypt_password() function in your answer.
"""

"""
Write a function that takes as argument a string and returns a new string in which the argument string has been altered using the 5 mentioned alterations. For example, "assignment" should be changed into "#@SS1GNMENT!".
Hint: You migth want to use the string.replace() method in your answer.
"""

def altere_password(s):
    altered_s = s.lower()
    altered_s = altered_s.replace('i', '1')
    altered_s = altered_s.replace('a', '@')
    
    altered_s = '#'+altered_s+"!"
    altered_s = altered_s.upper()
    return altered_s

s = "assignment"
altered_s = altere_password(s)
print(altered_s)