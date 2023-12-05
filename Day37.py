# Final keyword in Exception Handling

print("Final in  Exception handling")


def fun(index):
    print("Inside function")
    try:
        l = [2, 3, 4, 5]
        return 1
    except:
        print("Error occured")
        return 0
    finally:
        print("I;m always excute")


fun(5)
