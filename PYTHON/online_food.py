#Ordernow - Online Food Ordering System

#GREETINGS!
print("!!: Welcome to Ordernow :-!!")

#define the menu of restaurant
menu = {
    "pizza":150,
    "fried rice":120,
    "chicken":200,
    "roll":100,
    "burger":80
}
print("Pizza:Rs150\nFried Rice:120\nChicken:Rs200\nRoll:Rs100\nBurger:Rs80")
#order process
order_total=0
item_1=input("Enter the item you want to order:").strip().lower()
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"{item_1} added to your order. Price: Rs{menu[item_1]}")
else:
    print(f"ordered item {item_1} is not in the menu")
    
another_item=input("Do you want to order something else? (yes/no): ").strip().lower()
if another_item=="yes" or another_item=="y":
    another_item=input("Enter the item you want to order:").strip().lower()
    if another_item in menu:
        order_total+=menu[another_item]
        print(f"{another_item} added to your order. Price: Rs {menu[another_item]}")
    else:
        print(f"ordered_item {another_item} is not in the menu")
else:
    print("Thank you for your order!")
    print("Visit again!")
#salutation
print(f"your order total is Rs:{order_total}")     
print("Thank you for ordering from ordernow!")
print("Visit again!")   
