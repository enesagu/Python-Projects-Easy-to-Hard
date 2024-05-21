class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Create an instance of the Person class
person = Person("John", 30)

# Accessing private attributes directly will result in an error
# print(person.__name)  # AttributeError: 'Person' object has no attribute '__name'

# Using getter methods to access private attributes
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 30

# Using setter methods to modify private attributes
person.set_name("Jane")
person.set_age(25)

# Display updated information
person.display_info()  # Output: Name: Jane, Age: 25

# Attempting to set a negative age
person.set_age(-5)  # Output: Age must be positive
