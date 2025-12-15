months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

while True:
    Enter = int(input("Enter month number (1-12): "))
    if 1 <= Enter <= 12:
        print(f"The month is: {months.get(Enter)}")
        break
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
        Enter = int(input("Enter month number (1-12): "))

       
