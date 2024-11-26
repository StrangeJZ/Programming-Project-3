firstClass1 = [1, 2,"-----",3, 4]
firstClass2 = [5, 6,"-----",7, 8]
economyClass3  = [9, 10,"---",11, 12]
economyClass4 = [13, 14,"--",15, 16]
economyClass5 = [17, 18,"--",19, 20]

totalCheckout = []
takenSeats = []

class FirstClass:
    def __init__(self, fee):
        self.fee = fee

first_class = FirstClass(150)

class EconomyClass:
    def __init__(self, price):
        self.price = price

economy_class = EconomyClass(100)

print(firstClass1)
print(firstClass2)
print(economyClass3)
print(economyClass4)
print(economyClass5)

print("No seats are taken at this moment")

seat = int(input("Please select a seat that has not been taken: "))
if seat <= 8:
    totalCheckout.append(first_class.fee)
    takenSeats.append(seat)

elif seat >= 9:
    upgrade = int(input("Would you like to upgrade your seat to a first class seat? 1) Yes   2) No: "))
    if upgrade == 1:
        print(firstClass1)
        print(firstClass2)
        seat = int(input("Please select a seat in the first class section: "))
        totalCheckout.append(first_class.fee)
        takenSeats.append(seat)
    elif upgrade == 2:
        if seat == 9:
            print("This seat is placed in an Emergency Exit")
            aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
            if aknowledge == 2:
                seat = int(input("Please select a different seat: "))
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif aknowledge == 1:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
        elif seat == 12:
            print("This seat is placed in an Emergency Exit")
            aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
            if aknowledge == 2:
                seat = int(input("Please select a different seat: "))
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif aknowledge == 1:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
        elif seat == 11:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 10:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 13:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 14:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 15:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 16:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 17:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 18:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 19:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)
        elif seat == 20:
            totalCheckout.append(economy_class.price)
            takenSeats.append(seat)

print("Your seat has been added to the shopping cart")

extra = int(input("Would you like to add another seat? 1) Add another seat    2) Checkout: "))
if extra == 1:
    print(firstClass1)
    print(firstClass2)
    print(economyClass3)
    print(economyClass4)
    print(economyClass5)
    print("Taken Seats: ", takenSeats)
    seat = int(input("Please select a seat that has not been taken: "))
    if seat <= 8:
        totalCheckout.append(first_class.fee)
        takenSeats.append(seat)

    elif seat >= 9:
        upgrade = int(input("Would you like to upgrade your seat to a first class seat? 1) Yes   2) No: "))
        if upgrade == 1:
            print(firstClass1)
            print(firstClass2)
            print("Taken Seats: ", takenSeats)
            seat = int(input("Please select a seat in the first class section that has not been taken: "))
            totalCheckout.append(first_class.fee)
            takenSeats.append(seat)
        elif upgrade == 2:
            if seat == 9:
                print("This seat is placed in an Emergency Exit")
                aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
                if aknowledge == 2:
                    seat = int(input("Please select a different seat: "))
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif aknowledge == 1:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
            elif seat == 12:
                print("This seat is placed in an Emergency Exit")
                aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
                if aknowledge == 2:
                    seat = int(input("Please select a different seat: "))
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif aknowledge == 1:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
            elif seat == 11:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 10:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 13:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 14:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 15:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 16:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 17:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 18:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 19:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)
            elif seat == 20:
                totalCheckout.append(economy_class.price)
                takenSeats.append(seat)

    print("Your seat has been added to the shopping cart")
elif extra == 2:
    print("Taken Seats: ", takenSeats)
    print("Subtotal: $", sum(totalCheckout))
    print("Tax: $", float(sum(totalCheckout) * 0.065))
    print("Total: $", float(sum(totalCheckout) * 1.065))


while extra < 2:
    extra = int(input("Would you like to add another seat? 1) Add another seat    2) Checkout: "))
    if extra == 1:
        print(firstClass1)
        print(firstClass2)
        print(economyClass3)
        print(economyClass4)
        print(economyClass5)
        print("Taken Seats: ", takenSeats)
        seat = int(input("Please select a seat that has not been taken: "))
        if seat <= 8:
            totalCheckout.append(first_class.fee)
            takenSeats.append(seat)

        elif seat >= 9:
            upgrade = int(input("Would you like to upgrade your seat to a first class seat? 1) Yes   2) No: "))
            if upgrade == 1:
                print(firstClass1)
                print(firstClass2)
                print("Taken Seats: ", takenSeats)
                seat = int(input("Please select a seat in the first class section that has not been taken: "))
                totalCheckout.append(first_class.fee)
                takenSeats.append(seat)
            elif upgrade == 2:
                if seat == 9:
                    print("This seat is placed in an Emergency Exit")
                    aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
                    if aknowledge == 2:
                        seat = int(input("Please select a different seat: "))
                        totalCheckout.append(economy_class.price)
                        takenSeats.append(seat)
                    elif aknowledge == 1:
                        totalCheckout.append(economy_class.price)
                        takenSeats.append(seat)
                elif seat == 12:
                    print("This seat is placed in an Emergency Exit")
                    aknowledge = int(input("Do you agree to be of service during an emergency? 1)yes   2) No: "))
                    if aknowledge == 2:
                        seat = int(input("Please select a different seat: "))
                        totalCheckout.append(economy_class.price)
                        takenSeats.append(seat)
                    elif aknowledge == 1:
                        totalCheckout.append(economy_class.price)
                        takenSeats.append(seat)
                elif seat == 11:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 10:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 13:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 14:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 15:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 16:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 17:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 18:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 19:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)
                elif seat == 20:
                    totalCheckout.append(economy_class.price)
                    takenSeats.append(seat)

        print("Your seat has been added to the shopping cart")
    elif extra == 2:
        print("Taken Seats: ", takenSeats)
        print("Subtotal: $", sum(totalCheckout))
        print("Tax: $", float(sum(totalCheckout) * 0.065))
        print("Total: $", float(sum(totalCheckout) * 1.065))

