# Break and continue inside loops

# Break Statement
for i in range(12):
    if i == 10:
        break
    print("5X", i, "=", 5 * i)

# Continue Statement
for i in range(12):
    if i == 10:
        continue
    print("5X", i, "=", 5 * i)
