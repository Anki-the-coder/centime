import random
import string


def random_alphaNumeric(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))


def random_Numeric(size=10, chars=string.digits):
    return "".join(random.choice(chars) for x in range(size))


