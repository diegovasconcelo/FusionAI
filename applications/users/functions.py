# Extra functions
import random
import string

# Generate a Code for register
def code_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
