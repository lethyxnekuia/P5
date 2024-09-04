## Écrivez votre code ici !
class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def display_details(self):
        print(f"Nom: {self.name}")
        print(f"Âge: {self.age}")


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self.salary: float = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


person = Person(name="Maxime", age=29)
person.display_details()

employee = Employee(name="Maxime", age=29, salary=2000)
employee.display_details()
