my_list = list()
print(type(my_list))

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.append(50) 
my_list.append(60)
my_list.append(70)
print(my_list)

my_list.pop(-1)
print(my_list)

my_list.sort()
print (my_list)

print(my_list.index(30))
