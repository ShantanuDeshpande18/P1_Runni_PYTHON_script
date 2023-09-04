 # Declaring a list variable #
 # in Python list is lie as array #

cities = ["Kutch", "Pune", "Velavedar", "Kanha"]

print(cities)
print(type(cities))
print(cities[0])

cities.append("Nagpur")
print(cities)


cities.append(False)
print(cities)

cities.insert(1, "Sindh")
print (cities)

cities.insert (3 , "Sikkim")
print (cities)

cities.pop()
print(cities)

cities.pop(1)
print(cities)




for city in cities:
    print("The current value is:")
    print(city)


print("Process Comply")


clubs = ["RealMadrid", "ManUTD", "Bayern"]
for heritage in clubs:
    print(heritage)
