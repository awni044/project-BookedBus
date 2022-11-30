class PassengerRegistration():
 def __init__(self):
    self. Trip = ""
    self.seatNo = ""
 def Trip_destination(self):
    print("  buses ")
    print("1:Bus Number one:From Gaza to Rafah")
    print("2:Bus Number Two:From Ramallah to Bethlehem")
    print("3:Bus Number Third:From Jerusalem to Gaza")
    print("4:Bus Number Four:From Haifa to Jerusalem")
    self.a = int(input("Enter Number bus &destination"))
    if self.a == 1:
        self. Trip = "Bus Number one:From Gaza to Jerusalem"
    elif self.a == 2:
        self. Trip = "Bus Number Two:From Ramallah to Bethlehem"
    elif self.a == 3:
        self. Trip = "Bus Number Third:From Jerusalem to Gaza"
    elif self.a == 4:
        self. Trip = "Bus Number Four:From Haifa to Jerusalem"
    else:
        print("Please Enter correct choice  :")


 def booking_seats(self):

    seatNoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    self.bookingList = []
    self.seatNo = int(input("Choose a Seat Number :"))
    if self.seatNo != 0:
     if  self.seatNo < 15:
      self.seatNo in seatNoList
      self.bookingList.append(self.seatNo)
      del seatNoList[self.seatNo]
      count = len(seatNoList)
      print("The number of reserved seats:", self.bookingList)
     else:
         print("Error...the seat is not available")
    else:
        print("The number of seats is not available")

 def tickets_show(self):
     print("Your reservation has been confirmed")
     print("The passengerName",passengerName)
     print("The bus number",self. Trip)
     print("The number of seats reserved",self.bookingList)
p = PassengerRegistration()
passengerName = input("Enter Passenger Name :")
idpassenger = input("Enter Passenger ID :")
def Menu():
    print("********************* Welcome *********************************")
    print("********************Book bus tickets****************************")
    print("****************************************************************")
    print("   1-Display trips ")
    print("   2-Choose the number of seats")
    print("   3-tickets show   ")
    global choice
    choice = int(input("Please Entre yor choice"))

Menu()
while(True):
    if(choice==1):
        p.Trip_destination()
        n=input("Do you want to quit Y/N? ")
        if (n == "Y"):
            break
        else:
          Menu()

    elif(choice==2):
        p.booking_seats()
        n=input("Do you want to quit Y/N?")
        if (n == "Y"):
            break
        else:
            Menu()

    elif (choice == 3):
        p.tickets_show()
        n=input("Do you want to quit Y/N?")
        if (n == "Y"):
            break
        else:
            Menu()

    else:
        print("Wrong choice, choice 1 or 2 or 3 or 4")
        Menu()



