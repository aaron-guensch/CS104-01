# CS104
# Aaron Guensch
# conditions.py


temp = int(input("Please enter the current temperature: "))

#Providing clothing advice for different weather temperatures
if temp > 90:
    print("Wear Shorts")
elif temp > 70:
    print("Short sleeves are fine")
elif temp > 50:
    print("Wear a jacket")
elif temp > 32:
    print("Wear a heavy coat")
else:
    print("Stay Inside")
