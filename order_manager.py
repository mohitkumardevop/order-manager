import csv 

orders = []

with  open("orders.csv","r") as file:
   reader = csv.DictReader(file)
   for  row in reader:
          orders.append(row)

while  True:
     print("\n--- Order Manager ---")
     print("1. View all pending Orders")
     print("2. View overweight Orders")
     print("3.Add Order")
     print("4. Mark Order as delivered")
     print("5.Quit")
     
     choice = input("Choose an option: ")
      
     if choice =="1":
        for order in orders:
            if  order["delivered"] == "False":
               print(order)

     elif choice =="2":
        for order in orders:
            if float (order["weight"]) > 20:
                 print(order)

     elif choice == "3":
        order_id = input("Order ID: ")
        customer = input("Customer name: ")
        weight = input("Weight (kg): ")

        new_order = {
            "order_id": order_id,
            "customer": customer,
            "weight": weight,
            "delivered": "False"
        }

        orders.append(new_order)
        print("Order added.")

     elif choice == "4" :
          order_id = input("Order ID to mark as delivered: ")
          found = False
          
          for order in  orders:
              if order["order_id"] == order_id:
               order["delivered"] = "True"
               found = True
               print(f"Order {order_id} marked as delivered.")

          if not found:
                 print(f"Order {order_id} not found.")

     elif choice =="5":
           with open("orders.csv","w", newline="") as file:
              fieldnames =["order_id","customer","weight","delivered"]
              writer = csv.DictWriter(file, fieldnames=fieldnames)
              writer.writeheader()
              writer.writerows(orders)
           
           print("Changes saved to orders.csv.")
           break

     else :
           print("Invalid choice, try again.")


print("Program closed. ")

