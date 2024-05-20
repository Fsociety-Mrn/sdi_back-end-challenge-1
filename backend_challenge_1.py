
"""
    Size	    Seat Capacity	Cost (PHP)
    Small (S)	    5	           5000
    Medium (M)	    10	           8000
    Large (L)	    15	           12000
"""


class Car_Rental:
    def __init__(self):
        
        # Size = ( Seat Capacity, Cost (PHP) )
        self.car_small = ("S", 5, 5000)
        self.car_medium = ("M",10, 8000)
        self.car_Large = ("L",15, 12000)
        
        # self.car_small = ("S", 5, 5000)
        # self.car_medium = ("M", 9, 8000)
        # self.car_Large = ("L", 15, 11000)
        
    # Computation of rental car =============================================
    def __car_rental_computation(self,input):
        print("rental cost solution")
        size,seat,cost = self.car_small
        print(f"{size} x {input}")
        print(f"Total = PHP {cost*int(input)}")
        

    # Filter of user Input ==================================================
    def __cheapest_input(self,seat):
        
        if int(seat) <= 15 and int(seat) >= 1:
            print("accepted")
            print()
            return int(seat)
            
        
        print("not accepted")
        print()
        return self.__cheapest_input(max(seat))

        
    # Solution: if the inputed number are excedeed the seat capacity it only take the exceeded number
    def input_cheapest(self):
        seat = input("Please input number (seat): ")
        
        # input 2 digit number only
        if len(seat) > 2:
            print("2 input are max allow")
            print()
            return 
        data = self.__cheapest_input(seat)
        self.__car_rental_computation(data)
 
        
 

    # Main function
    def main(self):
        try:
            self.input_cheapest()
        except Exception as e:
            print("error: ", e)

while True:
    Car_Rental().main()


