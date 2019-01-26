x = [90, 10, 40, -20, -10, -40, 100]

pos = [i for i in x if i > 0]
neg = [i for i in x if i < 0]

print(pos + neg)
print(sorted(pos) + sorted(neg, reverse=True))
