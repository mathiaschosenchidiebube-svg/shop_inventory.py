choice=0
products=["Rice","Beans","Garri","Yam"]
prices={"Rice":300,"Beans":600,"Garri":1000,"Yam":700}
stock={"Rice":10,"Beans":4,"Garri":5,"Yam":7}
sales=[]
def total_sales(todays_sale):
        total=0
        for item, quantity in todays_sale:
         total+=prices[item]*quantity 
        return total
name=input("What's your name:")
print(f"WELCOME {name}")
while choice !=6:
    print("\n-- OUR MENU --")
    print("1.Add a new product")
    print("2.Record a sale")
    print("3.View all stock")
    print("4.Low stock report")
    print("5.Today's total sales")
    print("6.Quit")
    try:
        choice=int(input("Select Menu: "))
    except ValueError:
        print("Your selection can't be letters")
        continue 
    if choice==1:    
            item=input("What new product do you want to add: ").strip().title()
            while item=="" or not item.replace(" ", "").isalpha():
                print("Products can't be numbers and must be only letters")
                item=input("What new product do you want to add: ").strip().title()
            if item in products:
                print("You already have this product" )
                continue 
            products.append(item)
            while True:
                try:
                    price=int(input("Price: "))
                    if price <= 0:
                        print("Price can't be zero or equal to zero")
                    else:
                        prices[item]=price
                        print(prices)
                        break 
                except ValueError:
                     print("Enter a number")
            while True:
                try:
                    stocks=int(input("Stock:"))
                    if stocks < 0:
                        print("Stock can't be negative" )
                    else:
                        stock[item]=stocks
                        print(stock)
                        break
                except ValueError:
                    print("Enter a number ")
    elif choice==2:
        name=input("What product do you want to buy? ").strip().title()
        if name in stock:
            try:
                quantity=int(input("How many do you want to buy? "))
                if quantity<=0:
                    raise ValueError("The number cannot be zero or negative")
            except ValueError as e:
                print(e)
            else:
                if stock[name]>=quantity:
                    print("Thanks for your patronage")
                    stock[name]=stock[name]-quantity
                    print(f"Remaining stock of {name} is {stock[name]} ")
                    sales.append((name, quantity))
                    print(f"A customer came and bought {quantity} {name} now")
                    print(f"{len(sales)} customers served")
                else:
                    print(f"Insufficient stock of {name}, only {stock[name]} left")
        else:
            print("We do not sell it")
    elif choice==3:
        print(stock)
    elif choice==4:
         low_stock=[s for s in stock if stock[s] <=4]
         print(low_stock)
    elif choice==5:
       total=total_sales(sales)
       print(f"Today's sale is {total}")
    elif choice==6:
        total=total_sales(sales)
        if total>=7500:
            print("Today we made sales")
        elif total >=4500:
            print("Today wasn't bad")
        else:
            print("We try again tomorrow")
    else:
        print("Invalid choice. Select from 1-6")