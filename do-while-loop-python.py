
i = 0
choice = "y"

while i>=0:
    menu = int(input("enter your choice for menu : \n"))
    if menu == 1:
        print("""
            large pizza => 1900
            medium pizza => 1500
            small pizza => 100
        """)
    elif menu == 2:
        print("""
            zinger burger => 350
            finger chips => 100
            afghani burger => 250
        """)
    else:
        print("your choice is 1 or 2 only \n")
    choice = input("if you want to continue press y \n other wise press n \n")
    choice.lower()
    if choice == "y":
        continue
    else:
        break

