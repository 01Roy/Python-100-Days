# use of Super keyword


class ParentClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value from ParentClass: {self.value}")


class ChildClass(ParentClass):
    def __init__(self, value, additional_value):
        super().__init__(value)  # Calling the ParentClass __init__ method
        self.additional_value = additional_value

    def display_all(self):
        super().display()  # Calling the ParentClass method
        print(f"Additional Value: {self.additional_value}")


child = ChildClass(10, 20)
child.display_all()
