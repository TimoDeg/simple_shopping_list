shopping_list = []

def guide():
    print()
    print("Welcome to the Shopping List")
    print("----------------------------")
    print("Press 1 to add a new product")
    print("Press 2 to change a product")
    print("Press 3 to delete a product")
    print("Press 4 to view the product list")
    print("Press x to exit the program")
    print()

def add_product(product):
    print()
    shopping_list.append(product)
    print(f"The product '{product}' was added.")

def change_product(product):
    if product in shopping_list:
        new_product = input("New name for the product: ")
        shopping_list[shopping_list.index(product)] = new_product
        print(f"The product '{product}' was changed to '{new_product}'.")
    else:
        print(f"The product '{product}' does not exist.")

def delete_product(product): 
    print()
    if product in shopping_list:
        shopping_list.remove(product)
        print(f"The product '{product}' was deleted.")
    else:
        print(f"The product '{product}' does not exist.")

def show_list():
    print()
    for item in shopping_list:
        print(item, end=", ")
    print("\nThat's the list.")

def get_input():
    return input("Name of the product: ")

while True:
    guide()
    action = input("What would you like to do? ")

    match action:
        case "1":
            product = get_input()
            add_product(product)

        case "2":
            product = get_input()         
            change_product(product)

        case "3":
            product = get_input()
            delete_product(product)

        case "4":
            show_list()
        
        case "x":
            break
        
        case _:
            print("Unknown input. Make sure you enter the correct option.")
