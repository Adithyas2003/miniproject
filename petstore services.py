class pet:
    def _init_(s):
        print("Register")
    def name(s):
        print("Enter the pet name")
    def age(s):
        print("Enter the age")
    def species(s):
        print("Enter the species")
    def __str__(s):
        return f"{s.species}:{s.name},{s.age}"
class Dog(pet):
    print("Dog Details")
    def Dog_name(s):
        print("Enter Dog name")
    def Dog_age(s):
        print("Enter the Dog age")
    def Dog_breed(s):
        print("Enter the breed")
class cat(pet):
    print("cat details")
    def cat_name(s):
        print("Enter the  cat name")
    

