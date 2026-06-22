inventory = [
    {
        "name" :"notebook",
        "quantity" :20,
        "price" :float(1400.00),
    },

    {
        "name" : "Buckets",
        "quantity" : 35,
        "price" : float(1600.00),
    },

    {
        "name" : "coputer",
        "quantity" :25,
        "price" : float(95000.00),
    },
]
while True:
    print("You can do the following:\nA.Add new item\nB.View all items\nC.Update stock\nD.Remove an item\nE.Search an item by name\nF.Exit")

    choice=input("Choose an item between A,B,C,D,E or F: ").upper()

    if choice =="A":
        New_name= input("What item do you want to call your poroduct: ").lower()
        itemRepeated=False
        for items in inventory:
            if New_name==items["name"]:
                print("The item ia alread in the inventory")
                itemRepeated=True
                break
        if itemRepeated==False:
            try:
               New_Quantity=int(input("What is the quantity of the product: "))
               New_price=float(input("What is the price of the product: "))

               inventory.append({
                   "name":New_name,
                   "quantity":New_Quantity,
                   "price":New_price
               })
            except ValueError:
                print("please type an integer for the quantity and a decimal number for the price!")




    elif choice=="B":
        print("The items in your inventory are: ")
        for items in inventory:
            print(f"Name:{items['name']},Quantity:{items["quantity"]},Price:{items['price']}")




    elif choice=="C":
            item_changing=input("What item do you wnat to change: ").lower()

            item_changed=False

            for items in inventory:
                if items["name"]==item_changing:
                    item_category=input("Do you wan to change the name, quantity or the price; ")
                    item_changed=True
                    
                    if item_category=="name":
                        updateName=input("Input the new name: ").lower()
                        items["name"]=updateName
                    elif item_category=="quantity":
                        updateQuantity=input("Input new Quantity: ")
                        items["quantity"]=updateQuantity
                    elif item_category=="price":
                        updatePrice=input("Input new price: ")
                        items["price"]=updatePrice
                        break
                    else:
                        print("Invalid choice, try again")
            if item_changed==False:
                print("Item not found")   




    elif choice=="D":
            deleted_item=input("What is the name of the item you wany to delete: ").lower()

            deletion=False

            for items in inventory:
                if items["name"]==deleted_item:
                    inventory .remove(items)
                    print("Deleted successfully")

            if deletion ==False:
                print("Item was not found")




    elif choice=="E":
            searched=input("What is the item that you are looking for: ")

            is_searched=False
            
            for items in inventory:
                if searched in items["name"]:
                    print(f"The item is Name:{items['name']},Quantity:{items['quantity']},Price:{items['price']}")
                    is_searched=True
                    break
                if is_searched==False:
                    print("Item not found.")



    elif choice=="F":
            print("Goodbye!")
            break   
    

    else:
        print("Invalid choice! Try again")
    
