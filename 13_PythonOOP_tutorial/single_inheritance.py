'''

    date: 21.05.2024
    developer: Enes
    target: Signle Inheritance Programming 

'''


'''
    class name: Vehicle (Super Class / base)
   
'''


class Vehicle:

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    # return values of variables INIT

    def display_vehicle_info(self):

        return f"{self.brand} {self.model} {self.year}"

    def start_engine(self):

        return "Engine Start"


'''

    class name: Car (Drive Class)

'''


# first factor of inheritance
class Car(Vehicle):
    
    # second factor of inheritance
    def __init__(self, brand: str, model: str, year: int, num_of_doors: int):
        super().__init__(brand, model,year)
        self.num_of_doors = num_of_doors
        
    def displayHUD(self):
        hudDisplay = super().display_vehicle_info()
        return f"{hudDisplay} with {self.num_of_doors} doors"
    
    def bimbo(self):
        return "BEEP"
    
    
if __name__ == '__main__':
    '''
        Method resolution order
    '''
    
    car = Car("BMW", "XL","2024",2)
    
    
    
    
    
    
    
    