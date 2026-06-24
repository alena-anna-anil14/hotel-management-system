# HOTEL MANAGEMENT SYSTEM

# Customer Database
customers = {}

# Room Booking Database
room_bookings = {}

# Room Types
room_types = {
    1: ("Standard", 1000),
    2: ("Deluxe", 2000),
    3: ("Suite", 3000)
}

# Food Menu
food_menu = {
    1: ("Biriyani", 200),
    2: ("Fried Rice", 150),
    3: ("Burger", 120),
    4: ("Pizza", 300),
    5: ("Tea", 20),
    6: ("Coffee", 30)
}


# CUSTOMER REGISTRATION

def register_customer():

    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:
        print("Customer already registered!")
        return

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")

    customers[customer_id] = {
        "Name": name,
        "Phone": phone
    }

    print("Customer Registered Successfully!")


# ROOM BOOKING

def book_room():

    customer_id = input("Enter Customer ID: ")

    if customer_id not in customers:
        print("Customer not registered!")
        return

    room_no = int(input("Enter Room Number (101-110): "))

    if room_no in room_bookings:
        print("Room already booked!")
        return

    print("\n===== ROOM TYPES =====")
    print("1. Standard Room - Rs.1000/day")
    print("2. Deluxe Room - Rs.2000/day")
    print("3. Suite Room - Rs.3000/day")

    choice = int(input("Select Room Type: "))

    if choice in room_types:

        room_type, price = room_types[choice]

        room_bookings[room_no] = {
            "Customer ID": customer_id,
            "Room Type": room_type,
            "Price": price,
            "Days": 0,
            "Status": "Booked",
            "Food Bill": 0
        }

        print("Room Booked Successfully!")

    else:
        print("Invalid Room Type")


# CHECK IN

def check_in():

    room_no = int(input("Enter Room Number: "))

    if room_no in room_bookings:

        days = int(input("Enter Number of Days Stay: "))

        room_bookings[room_no]["Days"] = days
        room_bookings[room_no]["Status"] = "Checked-In"

        print("Check-In Successful!")

    else:
        print("Room not booked.")

# FOOD ORDERING

def order_food():

    room_no = int(input("Enter Room Number: "))

    if room_no not in room_bookings:
        print("Room not booked.")
        return

    print("\n===== FOOD MENU =====")

    for item, details in food_menu.items():
        print(item, ".", details[0], "- Rs.", details[1])

    choice = int(input("Select Food Item: "))
    quantity = int(input("Enter Quantity: "))

    if choice in food_menu:

        food_name, price = food_menu[choice]

        total = price * quantity

        room_bookings[room_no]["Food Bill"] += total

        print(food_name, "ordered successfully.")
        print("Food Cost: Rs.", total)

    else:
        print("Invalid Food Choice")


# CHECK OUT & BILLING

def check_out():

    room_no = int(input("Enter Room Number: "))

    if room_no not in room_bookings:
        print("Customer Record Not Found.")
        return

    booking = room_bookings[room_no]

    if booking["Status"] != "Checked-In":
        print("Customer has not checked in yet.")
        return

    customer = customers[booking["Customer ID"]]

    room_bill = booking["Days"] * booking["Price"]

    food_bill = booking["Food Bill"]

    total_bill = room_bill + food_bill

    print("\n================ BILL =================")
    print("Customer Name :", customer["Name"])
    print("Phone Number  :", customer["Phone"])
    print("Room Number   :", room_no)
    print("Room Type     :", booking["Room Type"])
    print("Days Stayed   :", booking["Days"])
    print("Room Charges  : Rs.", room_bill)
    print("Food Charges  : Rs.", food_bill)
    print("---------------------------------------")
    print("Total Bill    : Rs.", total_bill)
    print("=======================================")

    del room_bookings[room_no]

    print("Check-Out Successful!")


# VIEW CUSTOMER RECORDS

def view_records():

    if len(room_bookings) == 0:
        print("No Records Available.")
        return

    print("\n===== CUSTOMER RECORDS =====")

    for room, booking in room_bookings.items():

        customer = customers[booking["Customer ID"]]

        print("\nRoom Number :", room)
        print("Customer ID :", booking["Customer ID"])
        print("Name        :", customer["Name"])
        print("Phone       :", customer["Phone"])
        print("Room Type   :", booking["Room Type"])
        print("Status      :", booking["Status"])


# SEARCH CUSTOMER

def search_customer():

    room_no = int(input("Enter Room Number: "))

    if room_no in room_bookings:

        booking = room_bookings[room_no]

        customer = customers[booking["Customer ID"]]

        print("\nCustomer Found")
        print("Name :", customer["Name"])
        print("Phone:", customer["Phone"])

    else:
        print("Customer Not Found")


# UPDATE CUSTOMER DETAILS

def update_customer():

    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:

        customers[customer_id]["Name"] = input("Enter New Name: ")
        customers[customer_id]["Phone"] = input("Enter New Phone Number: ")

        print("Customer Details Updated Successfully!")

    else:
        print("Customer Not Found")


# DELETE CUSTOMER RECORD

def delete_record():

    room_no = int(input("Enter Room Number: "))

    if room_no in room_bookings:

        del room_bookings[room_no]

        print("Customer Record Deleted Successfully!")

    else:
        print("Record Not Found")


# VIEW FOOD ORDERS

def view_food_orders():

    print("\n===== FOOD ORDER SUMMARY =====")

    for room, booking in room_bookings.items():

        print("Room:", room,
              "| Food Charges: Rs.", booking["Food Bill"])


# ROOM AVAILABILITY

def room_availability():

    print("\n===== ROOM AVAILABILITY =====")

    for room in range(101, 111):

        if room not in room_bookings:

            print("Room", room, "- Available")

        elif room_bookings[room]["Status"] == "Booked":

            print("Room", room, "- Reserved")

        else:

            print("Room", room, "- Occupied")


# ADMIN CONTROL MENU

def admin_menu():

    while True:

        print("\n===== ADMIN CONTROL MENU =====")
        print("1. View Customer Records")
        print("2. Search Customer")
        print("3. Update Customer Details")
        print("4. Delete Customer Record")
        print("5. View Food Orders")
        print("6. View Room Availability")
        print("7. Back")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            view_records()

        elif choice == 2:
            search_customer()

        elif choice == 3:
            update_customer()

        elif choice == 4:
            delete_record()

        elif choice == 5:
            view_food_orders()

        elif choice == 6:
            room_availability()

        elif choice == 7:
            break

        else:
            print("Invalid Choice")

# ------------------------------
# MAIN MENU
# ------------------------------
while True:

    print("\n====================================")
    print("      HOTEL MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Customer Registration")
    print("2. Room Booking")
    print("3. Check-In")
    print("4. Food Ordering")
    print("5. Check-Out & Billing")
    print("6. Room Availability")
    print("7. Admin Control Menu")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        register_customer()

    elif choice == 2:
        book_room()

    elif choice == 3:
        check_in()

    elif choice == 4:
        order_food()

    elif choice == 5:
        check_out()

    elif choice == 6:
        room_availability()

    elif choice == 7:
        admin_menu()

    elif choice == 8:
        print("Thank You For Using Hotel Management System!")
        break

    else:
        print("Invalid Choice")
