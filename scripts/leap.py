n = 2104
if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
