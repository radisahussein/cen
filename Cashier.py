#main functions
import sys

def mainMenu(x,y,z,b,s,t,u):
    print("------------------------------")
    print("Cashier App \n")
    print("1. Transactions")
    print("2. Inventory")
    print("3. Report")
    print("4. Exit")
    print("------------------------------")

    selection = input("Select Menu: ")
    while True:
        if selection == "1":
            menu1(x,y,z,b,s,t,u)
            break
        elif selection == "2":
            menu2(x,y,z,b,s,t,u)
            break
        elif selection == '3':
            menu3(x,y,z,b,s,t,u)
            break
        elif selection == '4':
            sys.exit(1)

        else:
            print("No such menu!")

            mainMenu(x,y,z,b,s,t,u)
            break

def menu1(x,y,z,b,s,t,u):
    if len(x) == 0:
        print("------------------------------")
        print("No available items")
        mainMenu(x,y,z,b,s,t,u)

    else:
        print("------------------------------")
        print("Transaction Menu \n ")
        print("Balance:","Rp",str(b),"\n")
        print("1. Transaction")
        print("2. Back")
        print("------------------------------")
        selection = input("Select Menu: ")
        if selection == "1":
            transactionMenu(x,y,z,b,s,t,u)
        elif selection == "2":
            mainMenu(x,y,z,b,s,t,u)
        else:
            print("------------------------------")
            print("No such menu!")
            menu1(x,y,z,b,s,t,u)





def menu2(x,y,z,b,s,t,u):
    print("------------------------------")
    print("1. Add New Item")
    print("2. Add Stock")
    print("3. List of Items")
    print("4. Back")
    selection2 = (input("Select Menu: "))
    if selection2 == "1":
        addNewItem(x,y,z,b,s,t,u)

    elif selection2 == "2":
        addStock(x,y,z,b,s,t,u)

    elif selection2 == "3":
        listOfItems(x,y,z,b,s,t,u)

    elif selection2 == "4":
        mainMenu(x,y,z,b,s,t,u)

    else:
        print("------------------------------")
        print("No such menu!")
        menu2(x,y,z,b,s,t,u)
        

def menu3(x,y,z,b,s,t,u):
    reportTransaction(x,y,z,b,s,t,u)

def menu4():
    print("Bye!")
    sys.exit(1)

def addNewItem(x,y,z,b,s,t,u):
    print("------------------------------")
    newItem = str(input("Enter Item Name: "))
    if newItem in x:
        print(newItem,"is already in the menu!")
        menu2(x,y,z,b,s,t,u)
    else:
        x.append(newItem)
        position = x.index(newItem)
        itemPrice = input("Price of Item: ")
        z.insert(position,itemPrice)
        print("Item",newItem,"added to inventory!")
        y.insert(position,0)
        menu2(x,y,z,b,s,t,u)

def listOfItems(x,y,z,b,s,t,u):
    print("------------------------------")
    print("List of Items: ")
    if len(x) == 0:
        print("No items added yet!")
    else:
        if len(y) == 0:
            print("No stock added to inventory")
            menu2(x,y,z,b,s,t,u)
        else:
            for i in range(len(y)):
                print(y[i],x[i])

    menu2(x,y,z,b,s,t,u)


def addStock(x,y,z,b,s,t,u):
    print("------------------------------")
    selection3 = str(input("Add Stock to which item? : "))
    if selection3 in x:
        position = x.index(selection3)
        amount = int(input("How much? : "))
        y[position] += amount
        print("Added",amount,"of",selection3,"to inventory.")
        menu2(x,y,z,b,s,t,u)
    else:
        print("No item found..")
        menu2(x,y,z,b,s,t,u)

def transactionMenu(x,y,z,b,s,t,u):
    print("------------------------------")
    cartSelection = str(input("Item: "))
    cart = []
    if cartSelection in x:
        cartPosition = x.index(cartSelection)
        print("Stock =", y[cartPosition])
        if y[cartPosition] == 0:
            print("------------------------------")
            print("Stock not enough!")
            transactionMenu(x,y,z,b,s,t,u)
        else:
            cartAmount = int(input("How much?: "))
            if cartAmount > y[cartPosition]:
                print("------------------------------")
                print("Stock not enough!")
                menu1(x, y, z,b,s,t,u)
            else:
                print("------------------------------")
                cart.append(cartSelection)
                y[cartPosition] -= cartAmount
                added = (int(z[cartPosition]) * cartAmount)
                b += added
                print(cartAmount,cartSelection, "added to cart!")
                print(y[cartPosition],cartSelection,"left")
                print("Rp."+ str(added),"added to balance")

                if cartSelection in s:
                    t[cartPosition] += added
                    u[cartPosition] += cartAmount
                else:
                    s.append(cartSelection)
                    t.insert(cartPosition,cartAmount)
                    u.insert(cartPosition,added)



                menu1(x, y, z,b,s,t,u)
    else:
        print("------------------------------")
        print("Item not available!")
        menu1(x, y, z,b,s,t,u)


def reportTransaction(x,y,z,b,s,t,u):
    print("------------------------------")
    print("Report: \n")
    for i in range(len(s)):
        print(str(t[i]),str(s[i])," =","Rp.",str(u[i]))

    print("\n")
    print("1.Back")
    selection = input("Menu: ")

    if selection == "1":
        mainMenu(x,y,z,b,s,t,u)
    else:
        print("Menu Selection not found!")
        reportTransaction(x,y,z,b,s,t,u)


#Variables
items = []
stock = []
price = []
transactionItem = []
transactionAmount = []
transactionPrice = []

balance = 0

mainMenu(items,stock,price,balance,transactionItem,transactionAmount,transactionPrice)




