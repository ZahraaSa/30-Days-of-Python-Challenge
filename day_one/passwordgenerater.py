import string ,random
def passwordgenerate ():
    length =int(input("enter password length"))
    chars = string.ascii_letters + string.digits + string.punctuation 
    password="".join (random.choice(chars) for i in range (length))
    return password
print (passwordgenerate())
