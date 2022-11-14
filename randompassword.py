import random
cap = "QWERTYUIOPASDFGHJKLZXCVBNM"
low = "qwertyuiopasdfghjklzxcvbnm"
digits = "1234567890"
special="!#@$&_"
password = list()
password.extend(random.sample(cap , 2))
password.extend(random.sample(low , 2))
password.extend(random.sample(digits , 2))
password.extend(random.sample(special , 2))
random.shuffle(password)
password = "".join(password)
print(password)