#Void function will typically contain print function
#or have something terminal can output
def print_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

# This returns None by default because the function has no return statement
result = print_info("Murti", 21)
print("Function returned:", result)

def show_menu():
    print("1. Start")
    print("2. Exit")

show_menu()
