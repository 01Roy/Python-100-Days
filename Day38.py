# Raise Exceptio handling

a = input("Enter a state")

if a == "quite":
    print("we are good to go")
else:
    raise ValueError("The state is incoorect")
