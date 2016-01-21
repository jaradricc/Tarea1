import re

def singulariza(w):
    sing = re.sub('res','r', w)
    # sing = re.sub('ones$','on', sing)
    sing = re.sub('ses$','s', sing)
    sing = re.sub('ces$','z', sing)
    sing = re.sub('es$','', sing)
    return sing


w = raw_input("Ingresa la cadena en plural \n")
r = singulariza(w)
print r
