#!/usr/bin/python

import random 
import string

def RandomPasswordGenerator(passLen=10):
    generated_password = random.choice('?@!+*/')
    while len(generated_password) < passLen:
        generated_password += random.choice(string.ascii_letters)
    
    return generated_password
