my_list = [30, 10, 50, 20, 40]

my_list.sort()
print("Sorted list:", my_list)

my_list.sort(reverse=True)
print("Sorted list in descending order:", my_list)

new_list = sorted(my_list)
print("New sorted list:", new_list)
my_list.append(70)
print("New list:",my_list)
my_list.pop()
print(my_list)


