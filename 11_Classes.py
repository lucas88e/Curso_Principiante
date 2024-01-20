class Person:
    def __init__ (self, name, surname, alias ="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
    def walk(self):
        print(f"{self.full_name} está caminando")
    def showe(self):
        print(f"{self.full_name} se esta duchando")
    def eat(self):
        print(f"{self.full_name} esta comiendo un platano")


my_person =  Person("Lucas", "Madrid","Mwanos")
print(my_person.full_name)
my_person.walk()
my_person.eat()
my_person.showe()
my_other_person = Person("Cristiano", "Ronaldo", "Serresiete")
my_other_person.walk
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.showe()
my_other_person.full_name = "Juanito, Maravilla, El loco de los gatos"
my_other_person.walk()
my_other_person.eat()
my_other_person.full_name = 666
my_other_person.walk()
