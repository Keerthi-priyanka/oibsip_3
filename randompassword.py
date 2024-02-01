import random
Upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
symbol = '(){}@#%&:*'
number = '0123456789'
all_chars = lower + Upper + symbol + number

# Taking input for password length
length = int(input("Enter the desired password length"))

# Check if length is less than 8
if length < 8:
    print("Incorrect Password! Length should be at least 8.")
else:
    # Generate password
    password = "".join(random.sample(all_chars, length))
    print("The password generated is:", password)