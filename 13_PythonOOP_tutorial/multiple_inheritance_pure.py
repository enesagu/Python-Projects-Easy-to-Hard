'''

    date: 21.05.2024
    developer: Enes
    target: Signle Inheritance Programming 

'''


'''
    class name: Engine 
    param[1]: type of engine
    
'''


class Engine:
    def __init__(self, type_of_engine: str, **kwargs):
        super().__init__(**kwargs)
        
        self.type_of_engine = type_of_engine

    def start(self):
        return f"{self.type_of_engine} engine starting ..."


'''
    Transmission Class
'''


class Transmission:
    def __init__(self, type_of_transmission: str, **kwargs):
        super().__init__(**kwargs)
        
        self.type_of_transmission = type_of_transmission

    def operate(self):
        return f"{self.type_of_transmission} transmisson operating ..."


class Car(Engine, Transmission):

    def __init__(self, brand: str, type_of_engine:str, type_of_transmission:str):

        '''
        Engine.__init__(self, type_of_engine)

        Transmission.__init__(self, type_of_transmission)
        '''
        
        super().__init__(type_of_engine=type_of_engine, type_of_transmission = type_of_transmission)

        self.brand = brand

    def display_info(self):

        return f"{self.brand} car with {self.type_of_engine} with {self.type_of_transmission}"


if __name__ == "__main__":
    
    car = Car("Ford", "Petrol", "Automatic")
    
    print(car.display_info())
