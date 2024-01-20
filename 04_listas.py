my_list = list()


print(len(my_list))

my_list = [35, 24, 62 ,52, 30 ,30 ,17]
print(my_list)
print(len(my_list))
my_orther_list = [29, 1.77, "Lucas", "Madrid"]
print(my_orther_list)
print(my_orther_list[0:3])
age, height, name, surname = my_orther_list
print(name,age,height)
print(my_list+ my_orther_list)
my_orther_list.append("Morera")
print(my_orther_list)
my_orther_list.insert(1,"azul")
print(my_orther_list)
my_orther_list.remove("azul")
print(my_orther_list
      )
my_list.remove(30)
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(3)
print(my_list)
my_pop_element = my_list.pop(2)
print(my_pop_element)
my_list.sort()
print( my_list)