
def randomStringDigits(stringLength=6):
    import random
    import string

    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


print(randomStringDigits())