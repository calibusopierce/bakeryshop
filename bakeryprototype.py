print("USER VERIFICATION")
passcode = "123456"
input_pin = ""
while input_pin != passcode:
    input_pin = input("Enter Passcode: ")
else:
    print("\nCorrect Passcode, User Verified.")

print("\n\t\t------------------------------")
print("\t\t--  Welcome to the Pierce's --")
print("\t\t--          Bakery          --")
print("\t\t------------------------------")
print("\t\t--      [1] Pandesal        --")
print("\t\t--      [2] Monay           --")
print("\t\t--      [3] Pandecoco       --")
print("\t\t--      [4] Ensaymada       --")
print("\t\t--      [5] SpanishBread    --")
print("\t\t------------------------------")
bakerydict = {
        '1':{'Pandesal':'₱2' },
        '2':{'Monay': '₱3'},
        '3':{'Pandecoco': '₱4'},
        '4':{'Ensaymada': '₱4'},
        '5':{'Spanishbread':'₱4'}}
print(bakerydict)
order = input("\nEnter order: ")
if order == "1":
    print(f"[1]~Pandesal ₱2\n")
    pandesal = int("2")
    quantity = int(input("Enter the quantity of your order: "))
    order = (quantity * 2)
    print(f"The Total payment in your order is ₱{order}.00")
elif order == "2":
    print(f"[2]~Monay ₱3\n")
    quantity = int(input("Enter the quantity of your order: "))
    order = (quantity * 3)
    print(f"The Total payment in your order is ₱{order}.00")
elif order == "3":
    print(f"[3]~Pandecoco ₱4\n")
    quantity = int(input("Enter the quantity of your order: "))
    order = (quantity * 4)
    print(f"The Total payment in your order is ₱{order}.00")
elif order == "4":
    print(f"[4]~Ensaymada ₱4\n")
    quantity = int(input("Enter the quantity of your order: "))
    order = (quantity * 4)
    print(f"The Total payment in your order is ₱{order}.00")
elif order == "5":
    print(f"[5]~SpanishBread ₱4\n")
    quantity = int(input("Enter the quantity of your order: "))
    order = (quantity * 4)
    print(f"The Total payment in your order is ₱{order}.00")
else:
    print("INVALID SELECTION")

order2 = input("\t\nDo you want to buy other breads [yes] or [no]?: ")
if order2 == "yes":
    print("\t\t------------------------------")
    print("\t\t--  Welcome to the Pierce's --")
    print("\t\t--          Bakery          --")
    print("\t\t------------------------------")
    print("\t\t--      [1] Pandesal        --")
    print("\t\t--      [2] Monay           --")
    print("\t\t--      [3] Pandecoco       --")
    print("\t\t--      [4] Ensaymada       --")
    print("\t\t--      [5] SpanishBread    --")
    print("\t\t------------------------------")
    bakerydict = {
        '1':{'Pandesal':'₱2' },
        '2':{'Monay': '₱3'},
        '3':{'Pandecoco': '₱4'},
        '4':{'Ensaymada': '₱4'},
        '5':{'Spanishbread':'₱4'}}
    print(bakerydict)

    second_order = input("\nEnter order: ")
    if second_order == "1":
        print(f"[1]~Pandesal ₱2\n")
        pandesal = int("2")
        quantity = int(input("Enter the quantity of your order: "))
        second_order = (quantity * 2)
        print(f"The total payment in your First order is ₱{order}.00")
        print(f"The total payment in your Second order is ₱{second_order}.00")
        total_order = (order + second_order)
        print(f"The Total payment is ₱{total_order}.00")
        payment = int(input("Enter the amount of your payment:₱"))
        change = (payment - total_order)
        print(f"CHANGE: ₱{change}.00")
        print("\t\t---------------------------------")
        print("\t\t--     THANK YOU COME AGAIN!   --")
        print("\t\t---------------------------------")
    elif second_order == "2":
        print(f"[2]~Monay ₱3\n")
        quantity = int(input("Enter the quantity of your order: "))
        second_order = (quantity * 3)
        print(f"The total payment in your First order is ₱{order}.00")
        print(f"The total payment in your Second order is ₱{second_order}.00")
        total_order = (order + second_order)
        print(f"The Total payment is ₱{total_order}.00")
        payment = int(input("Enter the amount of your payment:₱"))
        change = (payment - total_order)
        print(f"CHANGE: ₱{change}.00")
        print("\t\t---------------------------------")
        print("\t\t--     THANK YOU COME AGAIN!   --")
        print("\t\t---------------------------------")
    elif second_order == "3":
        print(f"[3]~Pandecoco ₱4\n")
        quantity = int(input("Enter the quantity of your order: "))
        second_order = (quantity * 4)
        print(f"The total payment in your First order is ₱{order}.00")
        print(f"The total payment in your Second order is ₱{second_order}.00")
        total_order = (order + second_order)
        print(f"The Total payment is ₱{total_order}.00")
        payment = int(input("Enter the amount of your payment:₱"))
        change = (payment - total_order)
        print(f"CHANGE: ₱{change}.00")
        print("\t\t---------------------------------")
        print("\t\t--     THANK YOU COME AGAIN!   --")
        print("\t\t---------------------------------")
    elif second_order == "4":
        print(f"[4]~Ensaymada ₱4\n")
        quantity = int(input("Enter the quantity of your order: "))
        second_order = (quantity * 4)
        print(f"The total payment in your First order is ₱{order}.00")
        print(f"The total payment in your Second order is ₱{second_order}.00")
        total_order = (order + second_order)
        print(f"The Total payment is ₱{total_order}.00")
        payment = int(input("Enter the amount of your payment:₱"))
        change = (payment - total_order)
        print(f"CHANGE: ₱{change}.00")
        print("\t\t---------------------------------")
        print("\t\t--     THANK YOU COME AGAIN!   --")
        print("\t\t---------------------------------")
    elif second_order == "5":
        print(f"[5]~SpanishBread ₱4\n")
        quantity = int(input("Enter the quantity of your order: "))
        second_order = (quantity * 4)
        print(f"The total payment in your First order is ₱{order}.00")
        print(f"The total payment in your Second order is ₱{second_order}.00")
        total_order = (order + second_order)
        print(f"The Total payment is ₱{total_order}.00")
        payment = int(input("Enter the amount of your payment:₱"))
        change = (payment - total_order)
        print(f"CHANGE: ₱{change}.00")
        print("\t\t---------------------------------")
        print("\t\t--     THANK YOU COME AGAIN!   --")
        print("\t\t---------------------------------")
    else:
        print("INVALID SELECTION")
elif order2 == "no":
    print(f"The Total payment is ₱{order}.00")
    payment = int(input("Enter the amount of your payment:₱ "))
    paymentbd = order
    change = (payment - paymentbd)
    print(f"CHANGE: ₱{change}.00")
    print("\t\t---------------------------------")
    print("\t\t--     THANK YOU COME AGAIN!   --")
    print("\t\t---------------------------------")
