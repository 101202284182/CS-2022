import random
from math import pi

# TASK 1
age = 16
print("%s? What a great age!\n" % (age))

# TASK 2
int1 = round(random.uniform(1, 100), 2)
int2 = round(random.uniform(1, 100), 2)
print("Int1: %.2f, Int2: %.2f;\nSum: %.2f;\nDifference: %.2f\nProduct: %.2f\n" % (int1, int2, int1 + int2, int1 - int2, int1 * int2))

# TASK 3
int1 = random.uniform(1, 100)
int2 = random.uniform(1, 100)
print("Int1: %f, Int2: %f;\nAVG: %f;\nRemainder: %f;\nFirst to the power of the second: %f\n" % (int1, int2, (int1 + int2)/2, int1 % int2, int1**int2))

# TASK 4
fahrenheit = 87
celsius = (5/9) * (fahrenheit - 32)
print("Fahrenheit: %d, Celsius: %d\n" % (fahrenheit, celsius))

# TASK 5
distance = 14021 # km
price = 900
totalPrice = distance * price
print("Total price: %d€\n" % (totalPrice))

# TASK 6
r = random.randint(1, 100)
h = r*2
volume = pi*r**2*h

totalLiquid = volume*random.randint(2, 900)

print("Volume per cylinder: %d, Total liquid: %d;\nTotal cylinders needed: %d\n" % (volume, totalLiquid, totalLiquid % volume))

# TASK 7
earthWeight = random.randint(20, 90)
moonWeight = earthWeight * 0.165
print("Earth weight: %d, Moon weight: %d\n" % (earthWeight, moonWeight))