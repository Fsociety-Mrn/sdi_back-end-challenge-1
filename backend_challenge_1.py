
import os

"""

    Size	    Seat Capacity	Cost (PHP)
    Small (S)	    5	           5000
    Medium (M)	    10	           8000
    Large (L)	    15	           12000
"""

"""
** (Optional) Extra points,

Also try to write another version of the solution that can support generic number of seat and cost. For example:

If the Medium size car seating capacity is changed from 10 to 9 OR
If the Large size car cost is changed from 12,000 to 11,000 OR both values are changed, your solution will still find the cheapest cost.
"""


class Car_Rental:
    def __init__(self):
        
        # Size = ( Seat Capacity, Cost (PHP) )
        self.car_info = {
                'small': {'size': 'S', 'seat': 5, 'cost': 5000},
                'medium': {'size': 'M', 'seat': 10, 'cost': 8000},
                'large': {'size': 'L', 'seat': 15, 'cost': 12000},
            }
        
        # (Optional) 
        self.car_info = {
                'small': {'size': 'S', 'seat': 5, 'cost': 5000},
                'medium': {'size': 'M', 'seat': 10, 'cost': 8000},
                'large': {'size': 'L', 'seat': 15, 'cost': 12000},
            }
        
        
    # Computation of rental car =============================================
    def __rental_computation_process(self,input,size,cost):
        print(f"{size} x {int(input)}")
        print(f"Total = PHP {cost*int(input)}")

        
    def __car_rental_computation(self,input,size):
        
        car_size = self.car_info[size]['size']
        car_cost = self.car_info[size]['cost']
        
        self.__rental_computation_process(size=car_size,cost=car_cost,input=input)
        
   

    # Filter of user Input ==================================================
    def __filter_input_filter(self,input):
        
        input_seat = []

        for key,data in self.car_info.items():
            input_seat.append((
                    input/ int(data['seat']),
                    key
                ))

        print(input_seat)
        
        # custom filter input
        if min(input_seat)[0] < 1:
            return (input/5, 'small')
        
        if min(input_seat)[0] < 2 and min(input_seat)[0] >= 1:
            return (input/10,'medium')
        
        if min(input_seat)[0] <= 3 and min(input_seat)[0] >= 2:
            return (input/15,'large')
        
        print(min(input_seat))
        return min(input_seat)
                
        
    def input_cheapest(self):
        seat = input("Please input number (seat): ")
        
        # input 2 digit number only
        if len(seat) > 2:
            print("2 input are max allow")
            print()
            return 
        
        
        # filter the input data
        input_size,size = self.__filter_input_filter(input=int(seat))
        
        # process the input data
        self.__car_rental_computation(input=int(input_size),size=size)
        

        
    # Main function
    def main(self):
        try:
            # Input filter function
            self.input_cheapest()            
            self.clear_screen()
        except Exception as e:
            print("error: ", e)
            self.clear_screen()
    
    # Clear Screen ==================================================
    def clear_screen(self):
        print()
        input("press enter to continue")
        os.system('cls')
     

while True:
    Car_Rental().main()
    



