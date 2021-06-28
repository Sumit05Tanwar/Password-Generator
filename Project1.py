import string
import random
if __name__ =="__main__":
    # Lower Alphabet
    s1 = string.ascii_lowercase
    # Upper Alphabet
    s2 = string.ascii_uppercase
    # Number 
    s3 = string.digits
    #Puctuation
    s4 = string.punctuation

    # Taking lenght of password 
    lenght_letter = int(input("Lenght of password: "))
    #Mixing all string
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)

    # Selecting letter from string
    print("your password")
    print("".join(s[0:lenght_letter]))
    