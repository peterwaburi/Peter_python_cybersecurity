inventory = [
    {
        "name" : "soap",
        "quantity" : 20,
        "price" : 20.0,
    },

    {
        "name" : "juice",
        "quantity" : 15,
        "price" : 20.0,
    },
]



print("******Hello welcome to our minishop*******")
print("Here is our menu:--Press the number of the option that you want to choose.--")
    
print("\n1. Add new item\n 2. View all items\n 3. Update itemns stock\n 4. Delete item\n 5. Search by name\n 6. Exit\n")


choice =int(input("Enter your choice:"))

if choice == 1:
        print("Here you add  a new item with its quantity and price")
        name=input("name of item: ").capitalize()
        quantity=int (input("Enter the quantity:"))
        price=float (input("Enter the price: "))


        new_item =inventory.append({
            "name":name,
            "quantity":quantity,
            "price":price
        })
        print("---Here is thelist of the available items and your added item---")
        for m in inventory :
            print(m["name"],m["quantity"],m["price"])   
        # print(inventory)  
        # print(inventory)
       

    
elif choice==2 :
        print("Here are the items in stock")
        for m in inventory :
            print(m["name"],m["quantity"],m["price"])   
         

elif choice ==3 :
       print("We have added some new items checkthem out")
       print(inventory)
       

elif choice ==4 :
       print ("Item deleted succesfully")

elif choice == 5 :
       print("Enter the name of the item:")

else:
       print("exit")
       






