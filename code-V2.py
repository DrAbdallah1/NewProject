# Students’ IDs, Names:
##   Manar 44341
##   Ghaneemah 59745
# Course: CE364 Software Engineering Tools Laboratory 
# Section: F1


import string
import random
StaffArr   = []   #Staff Array
TrainArr   = []   #Train Array
BookingArr = []   #Booking Array
#database files
Staff_File   = "staff.txt"
Train_File   = "train.txt"
Booking_File = "booking.txt"

#Classes 
class Staff:
    def __init__(self, ID, Name, Role, Age, Address, Password):
        self.ID       = ID
        self.Name     = Name
        self.Role     = Role
        self.Age      = Age
        self.Address  = Address
        self.Password = Password
#***************************************************************
class Train:
    def __init__(self, TrainNum, Origin, Destination, TotalSeats, AvailSeats, Fare):
        self.TrainNum       = TrainNum
        self.Origin         = Origin
        self.Destination    = Destination
        self.TotalSeats     = TotalSeats
        self.AvailableSeats = AvailSeats
        self.Fare           = Fare
    #display information  
    def DisplayInfo(self):
        print("\t Train Number   : " + self.TrainNum)
        print("\t Origin         : " + self.Origin)
        print("\t Destination    : " + self.Destination)
        print("\t Total Seats    : " + self.TotalSeats)
        print("\t Available Seats: " + self.AvailableSeats)
        print("\t Fare           : " + self.Fare)
    #return information
    def GetData(self):
       TrainData = self.TrainNum    + ',' + self.Origin         + ',' + self.Destination +  ',' + \
                   self.TotalSeats  + ',' + self.AvailableSeats + ',' + self.Fare
       return TrainData 
#***************************************************************
class Booking:   
    def __init__(self, PNR, TrainNum, BerthNum, Origin, Destination, ID, Name, Age, Address):
        self.PNR         = PNR
        self.TrainNum    = TrainNum
        self.BerthNum    = BerthNum
        self.Origin      = Origin
        self.Destination = Destination
        self.ID          = ID
        self.Name        = Name
        self.Age         = Age
        self.Address     = Address
    #display information of the Booking 
    def DisplayInfo(self):
        print("\t PNR         : " + self.PNR)
        print("\t Train Number: " + self.TrainNum)
        print("\t Berth Number: " + self.BerthNum)
        print("\t Origin      : " + self.Origin)
        print("\t Destination : " + self.Destination)
        print("\t Civi lID    : " + self.ID)
        print("\t Name        : " + self.Name)
        print("\t Age         : " + self.Age)
        print("\t Address     : " + self.Address)  
    #return information
    def GetData(self):
        BookingData = self.PNR    + ',' + self.TrainNum     + ',' + self.BerthNum + ',' + \
                      self.Origin + ',' + self.Destination  + ',' + self.ID       + ',' + \
                      self.Name   + ',' + self.Age          + ',' + self.Address
        return BookingData
#==========================================================================================



#=================================  Read the files  ==========================================        
def Read_Database_Files():
    Read_Staff_File   = False
    Read_Train_File   = False
    Read_Booking_File = False
    #Read Staff File
    try:
        with open(Staff_File, "r") as File:    #open file
            Lines = File.readlines()           #read lines
            for line in Lines:
                Data = line.strip()            #split data in line
                ID, Name, Role, Age, Address, Password = Data.split(',')
                StaffInfo = Staff(ID, Name, Role, Age, Address, Password)
                StaffArr.append(StaffInfo)     #append data to array
            Read_Staff_File = True
    except:                                        #if error in open file
        print(" Error in open Staff file !") 
 
    #Read Train File
    try:
        with open(Train_File, "r") as File:    #open file
            Lines = File.readlines()           #read lines
            for line in Lines:
                Data = line.strip()            #split data in line
                TrainNum, Origin, Destination, TotalSeats, AvailSeats, Fare = Data.split(',')
                TrainInfo = Train(TrainNum, Origin, Destination, TotalSeats, AvailSeats, Fare)
                TrainArr.append(TrainInfo)     #append data to array
            Read_Train_File = True
    except:                                        #if error in open file
        print(" Error in open Train file !") 

    #Read Booking File
    try: 
        with open(Booking_File, "r") as File:   #open file
            Lines = File.readlines()            #read lines
            for line in Lines:
                Data = line.strip()             #split data in line
                PNR, TrainNum, BerthNum, Origin, Dest, ID, Name, Age, Address = Data.split(',')
                BookingInfo = Booking(PNR, TrainNum, BerthNum, Origin, Dest, ID, Name, Age, Address)
                BookingArr.append(BookingInfo)   #append data to array
            Read_Booking_File = True
    except:                                        #if error in open file
        print(" Error in open Booking file !") 

    if Read_Staff_File and Read_Train_File and Read_Booking_File:
        return True
    else:
        return False    
#=====================================================================================

    
#=================================  Update the files  ====================================     
def UpdateTrain_File():
    try:
        with open(Train_File, "w") as File:        #open file
            for i in range (len(TrainArr)):     
                Data = TrainArr[i].GetData()       #Get train informaiotn
                if i < len(TrainArr)-1:            #if no end informaiotn, add new line
                    Data = Data + '\n'  
                File.write(Data)                   #write data to file
            return True      
    except:                                        #if error in open file
        print(" Error in update Train file") 
        return False
#****************************   
def UpdateBooking_File():
    try:
        with open(Booking_File, "w") as File:      #open file
            for i in range (len(BookingArr)):
                Data = BookingArr[i].GetData()     #Get booking informaiotn
                if i < len(BookingArr)-1:          #if no end informaiotn, add new line
                    Data = Data + '\n'
                File.write(Data)                   #write data to file
            return True      
    except:                                        #if error in open file
        print(" Error in update Booking file")  
        return False
#****************************
def Update_Database_Files():
    if UpdateTrain_File() and UpdateBooking_File():
        return True
    else:
        return False        
#==================================================================================


                
#================================  A) Passenger ================================                
def Passenger():
    while True:   
        print("\n A1. Search & Book Train")      #display the Menu for Passenger
        print(" A2. Check Previous Booking")
        print(" A3. Back to Previous Menu")
        choice = input(" Please select: ")       #display the Menu for Passenger
        if choice == 'A1' or choice == 'a1':     #A1. Search & Book Train
            SearchBook_Train()                    #go to SearchBook_Train function
        elif choice == 'A2' or choice == 'a2':   #A2. Check Previous Booking
            CheckPrevious_Booking()               #go to CheckPrevious_Booking function
        elif choice == 'A3' or choice == 'a3':   #A3. Back to Previous Menu
            break                                 #back 
        else:                                    #if error in select
            print("Error in select !")

#**********************************************************
#A1. Search & Book Train
def SearchBook_Train():
    View_Recommend_Trains()   #Recommend Trains for user 
    Found = False
    x = 1
    Origin      = input("  Enter origin     : ")   #read origin 
    Destination = input("  Enter destination: ")   #read destination  
    for i in range(len(TrainArr)):
        if  TrainArr[i].Origin == Origin and TrainArr[i].Destination == Destination:    #if found 
            print("  The details of train " + str(x)+ ":")    #display Train information
            TrainArr[i].DisplayInfo()
            x = x + 1
            Found = True
            
    if Found == True:                                    #if found train
        choice = input("  Press (Y) to book a train: ")   #check is user need to book
        if choice == 'Y' or choice == 'y':
            TrainNum = input("  Enter Train number: ")   #read Train number
            for j in range(len(TrainArr)):
                if TrainArr[j].TrainNum == TrainNum:  #if train found
                    if int(TrainArr[j].AvailableSeats) > 0:  #if Available Seats found
                        #read user information
                        ID      = input("  Enter Civil ID    : ")
                        Name    = input("  Enter Name        : ")
                        Age     = input("  Enter Age         : ")
                        Address = input("  Enter Address     : ")
                        #Ggenerate Random 6-character alphanumeric PNR
                        charts  = string.ascii_letters + string.digits
                        PNR     = ''.join(random.choice(charts) for i in range(6))
                        #Generate Random 3-digit numerical Berth Number
                        BerthNum = ''.join(random.choice(string.digits) for i in range(3))

                        BookInfo = Booking(PNR, TrainNum, BerthNum, Origin, Destination, ID, Name, Age, Address)  #append to class
                        BookingArr.append(BookInfo)     #append to array
                        TrainArr[j].AvailableSeats = str(int(TrainArr[j].AvailableSeats) - 1)  #decrease Available Seats
                        if Update_Database_Files():      #Update Train and Booking File
                            print("     The booking is saved with reference (PNR):", PNR)
                    else:                                #if no Available Seats found
                        print("  No Available Seats !!")
                    break
    if Found == False:    #if no train found
       print("  No Available Trains !!")                   
#***************************************************
#Recommend_Trains for Search & Book Train
def View_Recommend_Trains():
    ID  = input("  Enter Civil ID     : ")  #read ID
    x = 1
    TrainsBooked = []
    Found = False
    print("  Recommended Trains:")
    for i in range(len(BookingArr)):
        if BookingArr[i].ID == ID:    #if user has previous booking
            Found = True
            if BookingArr[i].TrainNum not in TrainsBooked:
                TrainsTraveled.append(BookingArr[i].TrainNum)
                print("  #" + str(x) + ":")
                print("    Train Number :", BookingArr[i].TrainNum)
                print("    Berth Number :", BookingArr[i].BerthNum)
                print("    Origin       :", BookingArr[i].Origin)
                print("    Destination  :", BookingArr[i].Destination)
                x = x + 1
    if Found == False:
        print("     Not Found" )
#*****************************************************
#A2. Check Previous Booking
def CheckPrevious_Booking():
    PNR = input("  Enter booking reference(PNR): ")  #read PNR from user
    Found = False
    for i in range(len(BookingArr)): 
        if PNR == BookingArr[i].PNR:    #if PNR is found
            print("  Book found:")
            BookingArr[i].DisplayInfo() #display booking information
            choice = input("  Press (Y) to cancel this booking: ")
            if choice == 'Y' or choice == 'y':  # cancel booking 
                BookingArr.pop(i)        #delete Booking  
                UpdateBooking_File()     #update Booking File 
                print("     The booking is deleted")  
            Found = True
            break
    if Found == False:   #if PNR is not found 
        print("  The booking reference is not found !")      
#==============================================================================



#=============================  B) Ticket Inspector ============================                
def Ticket_Inspector_Menu():
    while True:   
        print("\n B1. Block Passenger")
        print(" B2. Back to Previous Menu")
        choice = input(" Please select: ")
        if   choice == 'B1' or choice == 'b1':  #B1. Block Passenger
            Block_Passenger()                    #go to Block_Passenger function
        elif choice == 'B2' or choice == 'b2':  #B2. Back to Previous Menu
            break                                #back 
        else:                                   #if error in select
            print(" Error in select !")
#*****************************************************
#B1. Block Passenger            
def Block_Passenger():
    ID = input("  Please enter passenger's civil ID: ")   #read civil ID
    Found = False
    for i in range(len(BookingArr)-1,-1, -1):  #check in Booking Array
        if ID == BookingArr[i].ID:             #if civil ID found
            print("   Booking is found")
            BookingArr[i].DisplayInfo()        #display Booking infrmation
            choice = input("   Press (Y) to block the booking: ")  # to block booking 
            if choice == 'Y' or choice == 'y':    
                BookingArr.pop(i)       #delete Booking  
                UpdateBooking_File()    #update Booking File 
                print("     The passenger booking is blocked")  
            Found = True
            break
    if Found == False:    #if civil ID not found
        print("  The passenger's civil ID is not found !")  
#==============================================================================



#===============================  C) Train Driver =============================         
def Train_Driver_Menu():
    while True:   
        print("\n C1. View Train Information")
        print(" C2. Cancel the Train")
        print(" C3. Train Report")
        print(" C4. Back to Previous menu")
        choice = input(" Please select: ")
        if   choice == 'C1' or choice == 'c1':   #C1. View Train Information
            View_Train_Information()              #go to View_Train_Information function
        elif choice == 'C2' or choice == 'c2':   #C2. Cancel the Train
            Cancel_Train()                        #go to Cancel_Train function
        elif choice == 'C3' or choice == 'c3':   #C3. Train Report
            Train_Report()                        #go to Train_Report function
        elif choice == 'C4' or choice == 'c4':   #C4. Back to Previous menu
            break
        else:
            print("Error in select !")   
#*****************************************************
#check if train found
def Ckeck_Train():
    FoundTrain  = False
    TrainIndex = -1
    TrainNum = input("  Please enter Train Number: ") #read Train Number from user
    for i in range(len(TrainArr)):                  
        if TrainArr[i].TrainNum == TrainNum:         #if Train Number found
            FoundTrain = True
            TrainIndex = i
            break
    if FoundTrain == False:                #if Train Number not found
        print("  No Train found for this Train number !")
    return FoundTrain, TrainIndex
#*****************************************************           
# C1. View Train Information
def View_Train_Information():
    FoundBooking = False
    FoundTrain, TrainIndex = Ckeck_Train()    #check if train found               
    if FoundTrain == True:         #if Train Number found            
        print("  The details of the Train:")
        TrainArr[TrainIndex].DisplayInfo()                #display train information
        print("   The details of the booking:")
        x = 1
        for i in range(len(BookingArr)):        #check booking
            if TrainArr[TrainIndex].TrainNum == BookingArr[i].TrainNum:  #if booking found
                FoundBooking = True
                print("     The details of passenger " + str(x) + ":")
                BookingArr[i].DisplayInfo()  #display Booking information
                x = x + 1
    if FoundBooking == False:              #if Booking Number not found
        print("   No Booking found for this Train number ")     
#*****************************************************
# C2. Cancel the Train
def Cancel_Train():
    FoundTrain, TrainIndex = Ckeck_Train()    #check if train found
    if FoundTrain == True:         #if Train Number found 
        print(" Train is found for this Train number")
        choice = input(" Press (Y) to cancel this Train: ")
        if choice == 'Y' or choice == 'y':           
            for j in range(len(BookingArr)-1,-1, -1):     #to delete Booking
                if TrainArr[TrainIndex].TrainNum == BookingArr[j].TrainNum: #if booking found
                    BookingArr.pop(j)           #delete Booking                   
            TrainArr.pop(TrainIndex)            #delete train 
            if Update_Database_Files():         #Update Train and Booking Files
                print("     The Train is deleted")
                print("     The booking for this train is deleted")              
#*****************************************************
# C3. Train Report
def Train_Report():
    print("  The details of Trains that are booked more than 90%:")
    x = 1
    for i in range(len(TrainArr)):
        if (int(TrainArr[i].AvailableSeats) / int(TrainArr[i].TotalSeats)) < 0.1:  #if booked > 90%
            print("    Train " + str(x) + ":")
            TrainArr[i].DisplayInfo()  #dsplay train information
            x = x + 1
#===================================================================================


            
#=================================  Login  ========================================= 
def LoginStaff():
    try:
        ID  = input(" Enter Civil ID : ")  #read Civil ID from user
    except:
        print(" Error in username !")
    try:
        Password = input(" Enter password: ")  #read password user
    except:
        print(" Error in password !")
   
    Found  = False
    for i in range(len(StaffArr)):  #check in staff array
        if StaffArr[i].ID == ID and StaffArr[i].Password == Password:  #if found          
            return StaffArr[i].Role, StaffArr[i].Name
    if Found == False :
        print(" Wrong ID or password !")
        return 0
#=====================================================================================


   
#===============================  Start Here  =======================================
if Read_Database_Files():      #if Read three files seucessful
    while True:   
        print("\n A. Passenger")
        print(" B. Login as Ticket Inspector ")
        print(" C. Login as Train Driver ")
        print(" D. Exit ")
        choice = input(" Please select: ")
        if   choice == 'A' or choice == 'a':    #A. Passenger 
            Passenger()                         #go to Passenger Menu
        elif choice == 'B' or choice == 'b':    #B. Login as Ticket Inspector 
             Role, Name = LoginStaff()          #login and get user role & name
             if Role == "Ticket_Inspector":     #if role is Ticket_Inspector
                 print(" Welcome: ", Name)    
                 Ticket_Inspector_Menu()        #go to Ticket_Inspector Menu
             else:                              #if role is not Ticket_Inspector
                 print(" Eoor in Role ! ")     
        elif choice == 'C' or choice == 'c':    #C. Login as Ticket Inspector 
             Role, Name = LoginStaff()          #login and get user role & name
             if Role == "Train_Driver":         #if role is Train_Driver
                 print(" Welcome: ", Name)
                 Train_Driver_Menu()            #go to Train_Driver Menu
             else:                              #if role is not Train_Driver
                 print(" Eoor in Role ! ") 
        elif choice == 'D' or choice == 'd':    #D. Exit 
            print(' The program will terminate ..')
            break
        else:                                   #Error in select
            print(" Error in select !")   




