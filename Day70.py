# class method as the alternative contructor


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))


# Using the alternative constructor
person1 = Person("Alice", 30)
person2 = Person.from_string("Bob,25")

print(person1.name, person1.age)  # Output: Alice 30
print(person2.name, person2.age)  # Output: Bob 25
