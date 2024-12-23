# Define the Person class.
class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print a message introducing the person
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Kenedy Kipkoech Rotich", 31, "Male")

# Call the introduce method to display the person's information
person1.introduce()
