def my_genrator():
    yield 1
    yield 2
    yield 3


gen = my_genrator()

for value in gen:
    print(value)
