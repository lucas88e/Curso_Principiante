def my_function():
    print("esto es una funcion")
my_function


def sum_two_values(first_number, second_number):
    print(first_number + second_number)

(sum_two_values("2","7"))

def sum_two_values_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_return (10, 5)
print(my_result)

def print_name (name, surname):
    print (f"{name} {surname}")

print_name("Lucas", "Madrid")    

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Lucas", "Madrid,")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Pythonm", "Lucas")
print(my_function)
