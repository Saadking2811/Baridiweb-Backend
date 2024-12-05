import random

def generate_ccp_code(length=8):
    """
    Generate a CCP code with the specified length.
    Default length is 8.
    """
    return ''.join(random.choices('0123456789', k=length))

def generate_cle(length=2):
    """
    Generate a CLE with the specified length.
    Default length is 2.
    """
    return ''.join(random.choices('0123456789', k=length))

# Example usage
ccp_code = generate_ccp_code()
cle = generate_cle()

print(f"Generated CCP code: {ccp_code}")
print(f"Generated CLE: {cle}")
