# About dir()

my_list = [1, 2, 3]
print(dir(my_list))  # Outputs list of attributes and methods of the 'list' object

# About __dict__


class MyClass:
    class_variable = 10

    def __init__(self):
        self.instance_variable = 20


obj = MyClass()
print(obj.__dict__)  # Outputs dictionary of instance attributes
print(MyClass.__dict__)  # Outputs dictionary of class attributes

# About help()

help(list)  # Displays help information for the 'list' class
help(obj)  # Displays help information for the 'obj' instance
