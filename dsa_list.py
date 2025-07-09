customers = []

for i in range (5):
    name = input(f"{i + 1}. Enter customer name: ")
    customers.append(name)
    
print("The customers are:")
for name in customers:
    print(name)
    
customers.sort()
print("The customers in alphabetical order are:")
print(customers)

search_name = input("Enter a name to search: ")
if search_name in customers:
    print(f"{search_name} is in the list.")
else:
    print(f"{search_name} is not in the list.")
