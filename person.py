class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes of the person
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Jay Dean", 29, "Male")

# Call the introduce method to display the person's information
person1.introduce()
