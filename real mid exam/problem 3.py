products = input().split("|")
command = input().split("%")
while not command[0] =="Shop!":

    if command[0] == "Important":
        if command[1] in products:
            products.remove(command[1])
            products.insert(0, command[1])
        else:
            products.insert(0, command[1])
    elif command[0] == "Add":
        if not command[1] in products:
            products.append(command[1])
        else:
            print("The product is already in the list.")
    elif command[0] == "Swap":
        if command[1] in products and command[2] in products:
            first_index = products.index(command[1])
            second_index = products.index(command[2])
            products[first_index],products[second_index] = products[second_index], products[first_index]
        else:
            if not command[1] in products:
                print(f"Product {command[1]} missing!")
            if not command[2] in products:
                print(f"Product {command[2]} missing!")
    elif command[0] == "Remove":
        if command[1] in products:
            products.remove(command[1])
        else:
            print(f"Product {command[1]} isn't in the list.")
    elif command[0] == "Reverse":
        products.reverse()
    command = input().split("%")

for index in range(len(products)):
    print(f"{index+1}. {products[index]}")