class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduction(self):
        return (f"Привет меня зовут'self.name', мне 'self.age' лет, я живу в 'self.city'")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Place of recidence: {self.city}"

person1 = Person("Aisen", 22, "Bishkek")
person2 = Person("Ilona", 17, "Bishkek")
person3 = Person("Ilona", 18, "Chernogory")

print(person1.is_adult())
print(person2.is_adult())
print(person3.is_adult())

print(person1)
